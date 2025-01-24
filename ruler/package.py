from sys import argv
from itertools import batched
from re import findall




# Packages provided to debootstrap --include
# Highly required
debootstrap_package_array = [
    "alsa-base",
    "alsa-topology-conf",
    "alsa-ucm-conf",
    "alsa-utils",
    "apt-utils",
    "bash-completion",
    "bc",
    "btop",
    "cloud-init",
    "cloud-initramfs-growroot",
    "cryptsetup-initramfs",
    "dbus",
    "debootstrap",
    "device-tree-compiler",
    "fakeroot",
    "fuse3",
    "gh",
    "git",
    "gnupg",
    "grub-efi-arm64",
    "initramfs-tools",
    "iptables",
    "jq",
    "landscape-common",
    "libfdt-dev",
    "libpython3-dev",
    "linux-firmware",
    "lm-sensors",
    "lshw",
    "lsof",
    "microcom",
    "nano",
    "nfs-kernel-server",
    "nvme-cli",
    "open-iscsi",
    "open-vm-tools",
    "openssh-client",
    "openssh-server",
    "openssh-sftp-server",
    "parted",
    "pciutils",
    "python-is-python3",
    "python3",
    "python3-automat",
    "python3-bcrypt",
    "python3-boto3",
    "python3-botocore",
    "python3-click",
    "python3-colorama",
    "python3-constantly",
    "python3-docutils",
    "python3-gdbm",
    "python3-hamcrest",
    "python3-hyperlink",
    "python3-incremental",
    "python3-launchpadlib",
    "python3-openssl",
    "python3-pip",
    "python3-pkg-resources",
    "python3-pyelftools",
    "python3-s3transfer",
    "python3-service-identity",
    "python3-setuptools",
    "python3-six",
    "python3-systemd",
    "python3-twisted",
    "python3-zope.interface",
    "python3.12-gdbm",
    "rfkill",
    "rsync",
    "software-properties-common",
    "squashfs-tools",
    "ssh-import-id",
    "udev",
    "udisks2",
    "uuid-runtime",
    "wireless-regdb",
    "wpasupplicant",
    "zerofree"
]


# Packages provided to debootstrap --exclude
# Don't install things you don't want
debootstrap_exclude_package_array = [
    "bluez"
]


# Oibuf's gpu driver packages
gpu_package_array = [
    "mesa-va-drivers",
    "mesa-vdpau-drivers",
    "mesa-vulkan-drivers",
    "vulkan-tools",
    "wayland-protocols"
]


# Package dependencies [bluez pipewire wireplumber liblc3]
pipewire_server_package_array = [
    "automake",
    "autotools-dev",
    "build-essential",
    "cmake",
    "doxygen",
    "libasound2-dev",
    "libavcodec-dev",
    "libavfilter-dev",
    "libavformat-dev",
    "libdbus-1-dev",
    "libdw-dev",
    "libebook1.2-dev",
    "libell-dev",
    "libfdk-aac-dev",
    "libffado-dev",
    "libfreeaptx-dev",
    "libgdbm-dev",
    "libglib2.0-dev",
    "libical-dev",
    "libjson-c-dev",
    "liblc3-dev",
    "libldacbt-abr-dev",
    "libldacbt-enc-dev",
    "libltdl-dev",
    "libmysofa-dev",
    "libncurses-dev",
    "libnss3-dev",
    "libopus-dev",
    "libpulse-dev",
    "libreadline-dev",
    "libsbc-dev",
    "libsdl2-dev",
    "libsndfile1-dev",
    "libssl-dev",
    "libsystemd-dev",
    "libtool",
    "libudev-dev",
    "libusb-1.0-0-dev",
    "libv4l-dev",
    "libva-dev",
    "libwebrtc-audio-processing-dev",
    "meson",
    "ninja-build",
    "pkg-config",
    "pulseaudio-utils",
    "rtkit",
    "systemd-dev",
    "v4l-conf",
    "v4l-utils"
]


# Cross compiler packages.
cross_compiler_packages = [
    "bc",
    "binfmt-support",
    "bison",
    "check",
    "cpio",
    "debhelper",
    "devscripts",
    "dh-make",
    "dkms",
    "dosfstools",
    "fakeroot",
    "fdisk",
    "findutils",
    "flex",
    "g++-aarch64-linux-gnu",
    "gawk",
    "gcc-aarch64-linux-gnu",
    "kmod",
    "libelf-dev",
    "ncurses-dev",
    "parted",
    "python3-distutils-extra",
    "qemu-efi-aarch64",
    "qemu-efi-riscv64",
    "qemu-system-arm",
    "qemu-user-static",
    "swig",
    "u-boot-tools",
    "udev",
    "uuid-runtime"
]


# Extra ackages on server
server_package_array = [
    "android-sdk-platform-tools",
    "aria2",
    "autofs",
    "ffmpeg",
    "gcc-arm-none-eabi",
    "git-lfs",
    "i2c-tools",
    "module-assistant",
    "mosh",
    "mpg123",
    "net-tools",
    "p7zip-full",
    "sshfs",
    "xz-utils"
]


# Extra packages on desktop
desktop_package_array = [
    "gnome-shell-extensions",
    "gnome-shell-extension-manager",
    "gnome-tweaks"
]




def parse_args():

    if "--debootstrap-include-packages" in argv:
        print(",".join(debootstrap_package_array))

        return

    if "--debootstrap-exclude-packages" in argv:
        print(",".join(debootstrap_exclude_package_array))

        return

    if "--server_essential_package_array" in argv:
        print(" ".join(server_essential_package_array))

        return

    if "--oibaf-gpu-packages" in argv:
        print(" ".join(gpu_package_array))

        return

    if "--pipewire-server-packages" in argv:
        print(" ".join(pipewire_server_package_array))

        return

    if "--additional-server-packages" in argv:
        print(" ".join(server_package_array))

        return

    return None




if __name__ == "__main__":
    parse_args()


# exit()

def encode_array(array, xlen=4):

    ylen = 1+(len(array) // xlen)

    array = [k for k in map(lambda x: [ len(max(x, key=lambda y: len(y))), x ], batched(array, ylen))]
    dump = ""
    for y in range(ylen):
        for x in range(xlen):
            try:
                # x*ylen+y
                n, k = array[x]
                dump += f'"{k[y]}"'.ljust(n+4)
            except IndexError:
                pass
        dump += "\n"
    return dump

def decode_array(dump, xlen=4):

    array = findall('"(.+)"', dump)

    darray = []

    ylen = (len(array) // xlen)+1
    rlen = (len(array)  % xlen)

    print(xlen, ylen, rlen)

    for x in range(xlen):
        for y in range(ylen):
            try:

                darray.append( array[x+y*xlen] )

            except IndexError:
                pass

    return darray

print(encode_array(debootstrap_package_array, xlen=4))
print(encode_array(pipewire_server_package_array, xlen=4))
print(encode_array(cross_compiler_packages, xlen=4))
print(dump:=encode_array(server_package_array, xlen=4))


# xz --decompress --stdout < ubuntu-image/ubuntu-24.10-preinstalled-server-arm64.img.xz | sudo dd of=/dev/nvme0n1 bs=8M iflag=fullblock oflag=direct status=progress

# Package syntax

# 6.12+nobara > 6.12 > 6.12.0~rc5-GITHUB_RUN_NUMBER

# pipewire-server_1.2.7+nobara-2ubuntu1_arm64.deb

