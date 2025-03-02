from sys import argv
from itertools import batched
from re import findall




# Server essential packages
server_essential_package_array = [
    "alsa-base",
    "alsa-topology-conf",
    "alsa-ucm-conf",
    "alsa-utils",
    "apt-utils",
    "bash-completion",
    "bc",
    # "bluez",
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
    # "landscape-common",
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
    "python3-colorama",
    "python3-docutils",
    "python3-openssl",
    "python3-pip",
    "python3-setuptools",
    "python3-six",
    "python3-systemd",
    "python3-venv",
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
    "libfftw3-dev",
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
server_extra_package_array = [
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




def parse_args(arg_array):

    try:
        separator_x = arg_array.index("--separator")
        separator = arg_array[separator_x+1]
        if separator not in set([" ", ",", ", "]):
            raise ValueError

    except ValueError:
        print('E: No --separator <,> <space> or <,space>')
        exit(1)


    package_dump_array = []

    if "--server-essential-packages" in argv:
        package_dump_array += server_essential_package_array

    if "--gpu-packages" in argv:
        package_dump_array += gpu_package_array

    if "--pipewire-server-packages" in argv:
        package_dump_array += pipewire_server_package_array

    if "--server-extra-packages" in argv:
        package_dump_array += server_extra_package_array

    print(separator.join(package_dump_array))

    return None




if __name__ == "__main__":
    parse_args(argv[1:])
