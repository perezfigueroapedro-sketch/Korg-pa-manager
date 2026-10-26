
[app]
title = Korg Pa Manager
package.name = korgpamanager
package.domain = com.pedro.korgpamanager
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.accept_sdk_license_agreements = True
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
p4a.bootstrap = sdl2
