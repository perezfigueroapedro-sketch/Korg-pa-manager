
[app]
title = Korg Pa Manager
package.name = korgpamanager
package.domain = com.pedro.korgmanager
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.buildtools_version = 33.0.2
android.accept_sdk_license_agreement = True
p4a.branch = master
