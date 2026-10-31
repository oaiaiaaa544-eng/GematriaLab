# GematriaLab Android

**Version 1.2** · Offline-first Android app · Package: `com.gematrialab.app`

## Features

- Multi-cipher calculator with selectable front-page cipher display. Selected ciphers are remembered on the device; the initial display uses the base four.
- Letter-by-letter breakdown, phrase comparison, date encoding matches and calculation history.
- Date calculator with date encodings, birthday intervals, offsets, and a multi-date comparison tool. Add as many dates as needed; the app calculates every pairwise interval.
- Number properties, factorization, divisors, digital roots and number representations.
- Custom A–Z cipher creator with local save.
- Dark charcoal, blue and teal calculator styling, inspired by Gematrinator's compact cipher-first layout.
- Runs offline; calculations and user selections remain on the device.

## Build

The GitHub Actions workflow `.github/workflows/build-android.yml` reconstructs the source archive, applies the UI/date update script in `.github/scripts/`, and builds a debug APK with Gradle 8.9.

To build manually:

1. Decode and extract `source-part-*.b64` into the `GematriaLabAndroid` project directory.
2. Apply the patch script from `.github/scripts/patch_app.py.gz.b64`.
3. Open the project in Android Studio or run `gradle assembleDebug`.

The APK artifact is named `GematriaLab-debug-apk` in GitHub Actions.

## App details

- Minimum Android: 7.0 (API 24)
- Compile SDK: 35
- Target SDK: 35
- Version code: 3
- Version name: 1.2

Some specialist cipher charts whose exact mappings have not been verified remain marked unavailable rather than displaying guessed values.
