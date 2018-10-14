# My Own Zsh Setting

* **Install `zsh`** 

Ubuntu : `$ sudo apt-get install zsh`

OS X : `$ brew install zsh`

* **change Shell `bash` to `zsh`**
> $ chsh -s `which zsh`

* **Install `Oh-My-Zsh`**
> $ curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh

* **Install `zsh-syntax-highlighting`**
> $ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
> $ echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc

And Copy my basic zshrc setting and "agnoster" theme which is added newline style. 
