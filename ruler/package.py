from sys import argv




# Packages provided to debootstrap --include
# Highly required
debootstrap_package_array = [
    "debootstrap",
    "linux-firmware",
    "cloud-initramfs-growroot",
    "grub-efi-arm64",
    "initramfs-tools",
    "cloud-init",
    "git",
    "bash-completion",
    "microcom",
    "nano",
    "btop",
    # "dbus",
    # "rfkill",
    # "rsync",
    "iptables",
    "apt-utils",
    "software-properties-common",
    "device-tree-compiler",
    "nvme-cli",
    "nfs-kernel-server",
    "python3",
    "python3-pip",
    "python3-pyelftools",
    "python3-setuptools",
    "python3-pkg-resources",
    "python3-docutils",
    "python3-launchpadlib",
    "python-is-python3",
    "libpython3-dev",
    "libfdt-dev",
    "alsa-topology-conf",
    "alsa-ucm-conf",
    "alsa-base",
    "alsa-utils"
]


# Packages provided to debootstrap --exclude
# Don't install things you don't want
debootstrap_exclude_package_array = [
    "bluez"
]


# Oibuf's gpu driver packages
gpu_package_array = [
    "mesa-vdpau-drivers",
    "mesa-va-drivers",
    "mesa-vulkan-drivers",
    "vulkan-tools",
    "wayland-protocols"
]


# Package dependencies [bluez pipewire wireplumber liblc3]
pipewire_server_package_array = [
    "autotools-dev",
    "automake",
    "build-essential",
    "cmake",
    "libtool",
    "libltdl-dev",
    "libasound2-dev",
    "libavcodec-dev",
    "libavfilter-dev",
    "libavformat-dev",
    "libfreeaptx-dev",
    "libfdk-aac-dev",
    "libopus-dev",
    "libffado-dev",
    "libldacbt-abr-dev",
    "libldacbt-enc-dev",
    "libpulse-dev",
    "libdbus-1-dev",
    "libusb-1.0-0-dev",
    "libglib2.0-dev",
    "libgdbm-dev",
    "libnss3-dev",
    "libsbc-dev",
    "libsdl2-dev",
    "libudev-dev",
    "libva-dev",
    "libv4l-dev",
    "libssl-dev",
    "libmysofa-dev",
    "libwebrtc-audio-processing-dev",
    "libncurses-dev",
    "libreadline-dev",
    "libsndfile1-dev",
    "libsystemd-dev",
    "libdw-dev",
    "libebook1.2-dev",
    "libell-dev",
    "libical-dev",
    "libjson-c-dev",
    "meson",
    "ninja-build",
    "pkg-config",
    "pulseaudio-utils",
    "doxygen",
    "rtkit",
    "systemd-dev",
    "v4l-utils",
    "v4l-conf"
]


# Cross compiler packages.
cross_compiler_packages = [
    "gcc-aarch64-linux-gnu",
    "g++-aarch64-linux-gnu",
    "check",
    "flex",
    "bison",
    "bc",
    "swig",
    "kmod",
    "cpio",
    "gawk",
    "dkms",
    "udev",
    "findutils",
    "dh-make",
    "debhelper",
    "devscripts",
    "fakeroot",
    "parted",
    "fdisk",
    "ncurses-dev",
    "u-boot-tools",
    "dosfstools",
    "uuid-runtime",
    "libelf-dev",
    "binfmt-support",
    "python3-distutils-extra",
    "qemu-user-static",
    "qemu-system-arm",
    "qemu-efi-aarch64",
    "qemu-efi-riscv64"
]


# Extra ackages on server
server_package_array = [
    "gcc-arm-none-eabi",
    "android-sdk-platform-tools",
    "p7zip-full",
    "aria2",
    "mosh",
    "net-tools",
    "i2c-tools",
    "mpg123",
    "ffmpeg",
    "sshfs",
    "autofs",
    "xz-utils",
    "module-assistant",
    "git-lfs"
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

    if "--oibaf-gpu-packages" in argv:
        print(" ".join(gpu_package_array))

        return

    if "--pipewire-server-packages" in argv:
        print(" ".join(pipewire_server_package_array))

        return

    if "--additional-server-packages" in argv:
        print(" ".join(server_package_array))


if __name__ == "__main__":
    parse_args()
    exit()



# xz --decompress --stdout < ubuntu-image/ubuntu-24.10-preinstalled-server-arm64.img.xz | sudo dd of=/dev/nvme0n1 bs=8M iflag=fullblock oflag=direct status=progress

# Package syntax

# 6.12+nobara > 6.12 > 6.12.0~rc5-GITHUB_RUN_NUMBER

"pipewire-server_1.2.7+nobara-2ubuntu1_arm64.deb"


crucial_packages_array = set(debootstrap_package_array + pipewire_server_array + cross_compiler_packages + gpu_extra_package + desktop_package_array)


linear_array = []
for package in server_package_array:
    if package not in crucial_packages_array:
        linear_array.append(package)
        print(f'    "{package}",')

