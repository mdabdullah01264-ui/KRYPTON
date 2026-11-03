# Krypton Launcher v2.4 — Real PojavLauncher (Android APK) & Desktop (Windows/Linux) Engine

This repository contains **both**:
1. **The Real Standalone Desktop & Termux/Linux Minecraft Launcher (`core/krypton_launcher_real.py`)**:
   - Downloads official Mojang `version_manifest_v2.json` (Classic, Alpha, Beta, 1.0 – 1.21.10+, Snapshots)
   - Multi-threaded downloader with SHA-1 verification for `client.jar`, Maven libraries, OS-specific LWJGL/Vulkan natives (`.dll`/`.so`), and game assets
   - Automatic **Fabric Loader** installer (`meta.fabricmc.net`)
   - Real **Modrinth v2 API** downloader for `.jar` Mods, `.mrpack` Modpacks, Shaders, and Resource Packs
   - Automatic **Eclipse Adoptium OpenJDK JRE 8, JRE 17, and JRE 21** downloader into `.minecraft/runtimes/Internal-JRE-{8,17,21}`
   - Uses the exact **PojavLauncher `.minecraft` directory layout** (`instances/`, `runtimes/`, `controlmap/`, `custom_env.txt`, `overrideargs.txt`)
   - Configures **Vulkan 1.3 (VulkanMod)**, **Krypton Zink (`MESA_LOADER_DRIVER_OVERRIDE=zink`)**, **MobileGlues**, **LTW**, and **HolyGL4ES**
2. **The Official PojavLauncher Android APK Fork & GitHub Actions Builder (`android_pojav_fork/` & `.github/workflows/build_krypton_all_platforms.yml`)**:
   - Clones `PojavLauncherTeam/PojavLauncher`, patches the **Krypton Purple Cosmic UI** (`#070312` deep space violet theme), embeds the Krypton UI & renderers, and compiles a real installable Android **`KryptonLauncher-arm64-v8a.apk`**, **`KryptonLauncher.exe` (Windows)**, and **`krypton-launcher` (Linux)**.

---

## How to Run on Windows or Linux Right Now

1. **Extract this ZIP** to any folder.
2. **Double-click `Start_Krypton_Windows.bat`** (on Windows) or run `./Start_Krypton_Linux_or_Termux.sh` (on Linux).
   - This starts the local native bridge at `http://127.0.0.1:28490` and opens the **Krypton Cosmic Purple UI** connected to the real Python downloader and JVM launcher!
3. **Or launch any Minecraft version directly from the terminal**:
   ```bash
   # Download & launch Minecraft 1.21.4 with Fabric + Vulkan native pipeline:
   python3 core/krypton_launcher_real.py --launch 1.21.4 --username ImranMd --renderer vulkan_native --ram 4096 --fabric

   # Download & install VulkanMod or Sodium from Modrinth into the Pojav instance:
   python3 core/krypton_launcher_real.py --install-mod vulkanmod --launch 1.21.4

   # Or open the native Tkinter Dark Purple GUI (zero browser needed):
   python3 core/krypton_launcher_real.py --tk
   ```

---

## How to Build the Real Android PojavLauncher `.apk` (Free via GitHub Actions)

1. Create a new GitHub repository and push the contents of this extracted folder to it.
2. Go to the **Actions** tab on GitHub and click **"Build Krypton Launcher (Android Pojav APK + Windows EXE + Linux AppImage)"** -> **Run workflow**.
3. GitHub Actions will automatically compile and upload:
   - `KryptonLauncher-Android-Pojav-APK` (`app_pojavlauncher-debug-arm64-v8a.apk`)
   - `KryptonLauncher-Windows-x64-EXE` (`KryptonLauncher.exe`)
   - `KryptonLauncher-Linux-x86_64` (`krypton-launcher`)
