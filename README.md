# Tutorial Instalasi dan Penggunaan Speedsnap

## Langkah 1.1: Instalasi Python

Pertama-tama, pastikan Python sudah terinstal di komputer Anda. Jika belum, Anda dapat mengunduh installer Python terbaru dari [situs resmi Python](https://www.python.org/downloads/).

- **Pastikan Anda memilih opsi "Add Python to PATH" saat menginstal.**

## Langkah 1.2: Instalasi Git

Pertama-tama, pastikan Git sudah terinstal di komputer Anda. Jika belum, Anda dapat mengunduh installer Git terbaru dari [situs resmi Git](https://git-scm.com/downloads/) dan menginstalnya.

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

## Langkah 4: Membuat Lingkungan Virtual
Di dalam folder proyek Speedsnap, buat sebuah lingkungan virtual Python untuk mengisolasi dependensi proyek. Jalankan perintah berikut:

```bash
virtualenv env
```

Perintah ini akan membuat folder 'env' yang berisi lingkungan virtual Python di dalam folder proyek Speedsnap.

## Langkah 5: Aktivasi Lingkungan Virtual
Setelah lingkungan virtual dibuat, aktifkan lingkungan tersebut dengan menjalankan perintah sesuai dengan sistem operasi Anda:

Windows
```bash
.\env\Scripts\activate
```

macOS & Linux
```bash
source env/bin/activate
```

## Langkah 6: Instalasi Dependensi
Di dalam folder speedsnap, Anda akan menemukan file requirements.txt yang berisi daftar paket Python yang diperlukan. Untuk menginstal semua dependensi ini, jalankan perintah berikut:

```bash
pip install -r requirements.txt
```


Untuk membuat akun admin di CLI pada proyek Speedsnap, Anda bisa mengikuti langkah-langkah berikut:

## Langkah 7: Buat Akun Admin
Setelah lingkungan virtual diaktifkan, Anda dapat membuat akun admin dengan menjalankan perintah berikut:

```bash
py manage.py createsuperuser
```
Perintah ini akan meminta Anda untuk memasukkan detail akun admin seperti username, alamat email (opsional), dan password. Setelah Anda mengisi informasi yang diperlukan, akun admin akan dibuat.

Setelah akun admin berhasil dibuat, Anda dapat menggunakan kredensial ini untuk masuk ke panel admin Speedsnap dan mengelola aplikasi sesuai kebutuhan Anda.

## Langkah 8: Jalankan Proyek
Sekarang, Anda dapat menjalankan proyek Speedsnap dengan menggunakan perintah berikut:

```bash
py manage.py runserver
```

Ini akan menjalankan server pengembangan lokal yang bisa diakses melalui browser.

## Langkah 9: Akses Lokalhost
Buka browser web Anda dan masukkan URL berikut:

```bash
http://localhost:8000/
```

Anda sekarang siap untuk menjelajahi aplikasi Speedsnap di lingkungan pengembangan lokal Anda!

Selamat mencoba!