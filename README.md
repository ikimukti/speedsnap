# Tutorial Instalasi dan Penggunaan Speedsnap

## Langkah 1: Instalasi Python

Pertama-tama, pastikan Python sudah terinstal di komputer Anda. Jika belum, Anda dapat mengunduh installer Python terbaru dari [situs resmi Python](https://www.python.org/downloads/).

- **Pastikan Anda memilih opsi "Add Python to PATH" saat menginstal.**

## Langkah 2: Instalasi Virtual Environment

Setelah Python terinstal, langkah selanjutnya adalah menginstal `virtualenv` untuk membuat lingkungan virtual Python yang terisolasi.

Buka terminal atau command prompt, dan jalankan perintah berikut:

```bash
pip install virtualenv
```

## Langkah 3: Membuat Lingkungan Virtual
Sekarang, buat lingkungan virtual di dalam folder proyek Anda. Pertama, clone repositori Speedsnap dari GitHub dengan perintah berikut:

```bash
git clone https://github.com/ikimukti/speedsnap.git
```

Setelah proses cloning selesai, masuk ke dalam folder speedsnap:

```bash
cd speedsnap
```

## Langkah 4: Instalasi Dependensi
Di dalam folder speedsnap, Anda akan menemukan file requirements.txt yang berisi daftar paket Python yang diperlukan. Untuk menginstal semua dependensi ini, jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

Setelah semua dependensi terinstal, Anda siap untuk menggunakan Speedsnap!

Selamat mencoba!
