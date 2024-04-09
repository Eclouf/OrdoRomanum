python3 -m venv venv
source venv/bin/activate

while test $# -gt 0
do
    case "$1" in
        --mac) echo "OS: Mac"
            ;;
        --debian) echo "OS: Debian"
            sudo apt install -y pkg-config python3-dev python3-venv libgirepository1.0-dev libcairo2-dev gir1.2-webkit2-4.0 libcanberra-gtk3-module
            ;;
    esac
    shift
done

pip3 freeze > requirements.txt
pip3 install -r requirements.txt