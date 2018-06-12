nodes=$(cat ./ips.txt)

src=$1
dst=$2

if [ -z $src ] || [ -z $dst ];then
    echo "Usage: $0 {src} {dst}"
    exit 1
fi

echo "Prepare to copy $src to $dst $nodes"

for ip in $nodes ; do
    echo
    echo $ip ---------------------------
    scp -o GSSAPIAuthentication=no -o ConnectTimeout=5 -r "$src" root@$ip:"$dst" && echo "OK"
done
