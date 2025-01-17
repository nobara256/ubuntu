from sys import argv




# Packages provided to debootstrap --include
debootstrap_package_array = [
    "debootstrap",
    "cloud-init",
    "git",
    "bash-completion",
    "microcom",
    "nano",
    "btop",
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

# Package dependencies to build Pipewire & Wireplumber
pipewire_server_array = [
    "cmake",
    "findutils",
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
    "systemd-dev",
    "v4l-utils",
    "v4l-conf"
]

# Cross compiler packages.
cross_compiler_packages = [
    "gcc-aarch64-linux-gnu",
    "check",
    "flex",
    "ncurses-dev",
    "bison",
    "g++-aarch64-linux-gnu",
    "swig",
    "u-boot-tools",
    "kmod",
    "cpio",
    "fakeroot",
    "parted",
    "udev",
    "dosfstools",
    "uuid-runtime",
    "fdisk",
    "bc",
    "dkms",
    "gawk",
    "dh-make",
    "devscripts",
    "debhelper",
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
    "build-essential",
    "gcc-arm-none-eabi",
    "android-sdk-platform-tools",
    "p7zip-full",
    "aria2",
    "rtkit",
    "rsync",
    "mosh",
    "rfkill",
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

# Oibuf's gpu driver packages
gpu_extra_package = [
    "mesa-vdpau-drivers",
    "mesa-va-drivers",
    "mesa-vulkan-drivers",
    "vulkan-tools",
    "wayland-protocols"
]



def parse_args():

    if "--debootstrap-include-packages" in argv:
        print(",".join(debootstrap_package_array))

        return

    if "--pipewire-server-packages" in argv:
        print(" ".join(pipewire_server_array))

        return


if __name__ == "__main__":
    parse_args()
    exit()



crucial_packages_array = set(debootstrap_package_array + pipewire_server_array + cross_compiler_packages + gpu_extra_package + desktop_package_array)


linear_array = []
for package in server_package_array:
    if package not in crucial_packages_array:
        linear_array.append(package)
        print(f'    "{package}",')

