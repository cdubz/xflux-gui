import os

# There is similar code in ./debian/postinst. If you are changing this
# you probably want to change that too.
def download_xflux():
    print("Downloading xflux12 ...")
    url = "https://justgetflux.com/linux/xflux12.tgz"
    tarchive = "/tmp/xflux12.tgz"
    os.system("wget '%s' -O'%s'" % (url, tarchive))
    os.system("tar -xvf '%s'" % tarchive)
    os.system("mv '%s' '%s'" % ('xflux12', 'xflux'))

if __name__ == '__main__':
    download_xflux()
