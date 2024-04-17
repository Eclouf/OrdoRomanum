python3 -m venv venv

while test $# -gt 0
do
    case "$1" in
        --windows) echo "OS: Windows"
            venv\Scripts\activate
            ;;
        --mac) echo "OS: Mac"
            source venv/bin/activate
            ;;
        --debian) echo "OS: Debian"
            source venv/bin/activate
            sudo apt install -y pkg-config python3-dev python3-venv libgirepository1.0-dev libcairo2-dev gir1.2-webkit2-4.0 libcanberra-gtk3-module
            ;;
    esac
    shift
done

pip3 install -r requirements.txt