#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<math.h>
#include<omp.h>
#include<stdint.h>
#include <time.h>
#include <mach/mach_time.h>

typedef uint8_t BYTE;
typedef uint32_t DWORD;
typedef int32_t LONG;
typedef int64_t LONGLONG;

typedef union _LARGE_INTEGER {
  struct {
    DWORD LowPart;
    LONG  HighPart;
  };
  struct {
    DWORD LowPart;
    LONG  HighPart;
  } u;
  LONGLONG QuadPart;
} LARGE_INTEGER, *PLARGE_INTEGER;

double GetCurrentTime(){
    static mach_timebase_info_data_t sTimebaseInfo;

    uint64_t  time = mach_absolute_time();

    uint64_t  nanos;

    if (sTimebaseInfo.denom == 0) {
        (void)mach_timebase_info(&sTimebaseInfo);
    }
    nanos = time * sTimebaseInfo.numer / sTimebaseInfo.denom;

    return ((double)nanos / 1000000000.0);
}

void grad_x(float* output, float* input, int width, int height){
    assert(output!=NULL && input!=NULL && width>0 && height>0);

    int w1 = width - 1;
    int h1 = height - 1;

    int i, j;

    for (i=0; i<height; ++i){
        j=0;
        output[j + (i*width)] = input[j+1 + (i*width)] - input[j + (i*width)];
        for (j=1; j<w1; ++j){
            output[j + (i*width)] = 0.5f * (input[j+1 + (i*width)] - input[j-1 + (i*width)]);
        }
        output[j + (i*width)] = input[j + (i*width)] - input[j-1 + (i*width)];
    }

}

void grad_y(float* output, float* input, int width, int height)
{
	assert(output!=NULL && input!=NULL && width>0 && height>0);

	int w1=width-1;
	int h1=height-1;

	int i, j;

	i=0;
	for (j=0;j<width;++j)
	{
		output[j+i*width]=input[j+(i+1)*width]-input[j+i*width];
	}
	for (i=1;i<h1;++i)
	{
		for (j=0;j<width;++j)
		{
			output[j+i*width]=0.5f*(input[j+(i+1)*width]-input[j+(i-1)*width]);
		}
	}
	for (j=0;j<width;++j)
	{
		output[j+i*width]=input[j+i*width]-input[j+(i-1)*width];
	}
}

int main(){
    omp_set_num_threads(4);

    int width = 1920;
    int height = 1080;
    double start_time;
    double end_time;

    int len = width * height;

    float* data = (float*)malloc(sizeof(float)*len);
    float* gx = (float*)malloc(sizeof(float)*len);
    float* gy = (float*)malloc(sizeof(float)*len);

    FILE* fp = fopen("./image.dat", "rb");
    fread(data, sizeof(float), len, fp);
    fclose(fp);

    LARGE_INTEGER Frequency;
    LARGE_INTEGER BeginTime;
    LARGE_INTEGER EndTime;

    start_time = GetCurrentTime();
    grad_x(gx, data, width, height);
    grad_y(gy, data, width, height);
    end_time = GetCurrentTime();

    printf("%lf\n", end_time-start_time);
}