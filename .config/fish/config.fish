fish_add_path $HOME/.spicetify $HOME/.local/bin $HOME/.local/scripts

alias vim='nvim'
alias ls='lsd --group-directories-first'
alias ll='ls -hlA'
alias l='ls -l'
alias fishcfg='nvim $HOME/.config/fish/config.fish'
alias fdisks='df --total --block-size=G | grep dev/nv --color=never'
alias myps='watch ps o pid,ppid,stat,comm'
alias neofetch="fastfetch"
alias ....="cd ../../../"
alias ...="cd ../../"
alias  ..="cd ../"
alias logouth="hyprclt dispatch exit"
alias encrypt="openssl enc -aes-256-cbc -in"
alias decrypt="openssl enc -d -aes-256-cbc -in"
alias muc="muc --file /home/ayx/.local/share/fish/fish_history.raw"
alias demo="xwaylandvideobridge"
alias gi="git init"
alias gsw="git show"
alias gd="git diff"
alias sg="git status"
alias ga="git add"
alias gb="git branch"
alias gr="git remote"
alias cg="git commit"
alias gpl="git pull"
alias gp="git push" 
alias gl="git log --graph --oneline --decorate --all"
alias gsub="git submodule update --recursive --remote"
alias suckless="colorscript -e 47 | head -n +4"
alias wh="which"
alias gt="gotop"
alias recentfile="recentfile -n1"
alias sxiv="nsxiv"
alias code="vscodium"
alias tsniff="sudo python /opt/garbage/capture.py"
alias nazi="nvim"
