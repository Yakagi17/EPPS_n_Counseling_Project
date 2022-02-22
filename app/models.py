from app import db
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Fakultas(UserMixin, db.Model):
    __tablename__ = 'Fakultas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_fakultas = db.Column(db.String(64))


class Prodi(UserMixin, db.Model):
    __tablename__ = 'Prodi'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_prodi = db.Column(db.String(64))
    jenjang = db.Column(db.String(64))
    id_fakultas = db.Column(db.Integer, ForeignKey('Fakultas'))


class Mahasiswa(UserMixin, db.Model):
    __tablename__ = 'Mahasiswa'

    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(64), nullable=False)
    nama_panggilan = db.Column(db.String(64), nullable=False)
    jenis_kelamin = db.Column(db.String(16), nullable=False)
    tanggal_lahir = db.Column(db.Date)
    email = db.Column(db.String(64), nullable=False)
    no_hp = db.Column(db.String(16), nullable=False)
    no_wa = db.Column(db.String(16), nullable=False)
    id_prodi = db.Column(db.Integer, ForeignKey('Prodi'), nullable=False)
    angkatan = db.Column(db.Integer)
    username = db.Column(db.String(64))

    def set_password(self, password_hash):
        self.password_hash = generate_password_hash(password_hash)
    
    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)

    def __repr__(self):
        return '<mahasiswa {}>'.format(self.name)


class StatusKonselor(UserMixin, db.Model):
    __tablename__ = 'Status_Konselor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(16))


class Konselor(UserMixin, db.Model):
    __tablename__ = 'Konselor'

    id = db.Column(db.Integer, primary_key=True) 
    nama_lengkap = db.Column(db.String(64), nullable=False)
    nama_panggilan = db.Column(db.String(64), nullable=False)
    jenis_kelamin = db.Column(db.String(16), nullable=False)
    tanggal_lahir = db.Column(db.Date)
    email = db.Column(db.String(64), nullable=False)
    no_hp = db.Column(db.String(16), nullable=False)
    no_wa = db.Column(db.String(16), nullable=False)
    id_status_konselor = db.Column(db.Integer, ForeignKey('Status_Konselor'), nullable=False)
    username = db.Column(db.String(64))

    def set_password(self, password_hash):
        self.password_hash = generate_password_hash(password_hash)
    
    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)

    def __repr__(self):
        return '<mahasiswa {}>'.format(self.name)


class JadwalMingguanKonselor(UserMixin, db.Model):
    __tablename__ = 'Jadwal_Mingguan_Konseling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_konselor = db.Column(db.Integer, ForeignKey('Konselor'), nullable=False)
    hari =  db.Column(db.String(16))
    waktu = db.Column(db.DateTime)
    durasi = db.Column(db.Integer)


class StatusService(UserMixin, db.Model):
    __tablename__ = 'Status_Service'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(64))

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(16))


class KategoriPembatalan(UserMixin, db.Model):
    __tablename__ = 'Kategori_Pembatalan'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(64))


class Pembatalan(UserMixin, db.Model):
    __tablename__ = 'Pembatalan'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_kategori_pembatalan = db.Column(db.Integer, ForeignKey('Kategori_Pembatalan'), nullable=False)
    keterangan = db.Column(db.Text)


class RoomMeeting(UserMixin, db.Model):
    __tablename__ = 'Room_Meeting'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_platform_meeting = db.Column(db.Integer, ForeignKey('Platform_Room_Meeting'), nullable=False)
    link = db.Column(db.String(255))
    password = db.Column(db.String(255))

class PlatformRoomMeeting(UserMixin, db.Model):
    __tablename__ = 'Platform_Room_Meeting'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(64))


class KonfirmasiKonseling(UserMixin, db.Model):
    __tablename__ = 'Konfirmasi_Konseling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal_konfirmasi = db.Column(db.DateTime)
    nip = db.Column(db.Integer, ForeignKey('Admin'), nullable=False)
    id_permintaan_jadwal_konseling = db.Column(db.Integer, ForeignKey('Permintaan_Jadwal_Konseling'), nullable=False)
    id_room_meeting = db.Column(db.Integer, ForeignKey('Room_Meeting'), nullable=False)
    link_room_meeting = db.Column(db.String(255))
    id_hasil_konseling = db.Column(db.Integer, ForeignKey('Hasil_Konseling'), nullable=True)


class StatusPenjadwalanKonseling(UserMixin, db.Model):
    __tablename__ = 'Status_Konseling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_status_penjadwalan = db.Column(db.String(16))


class PermintaanService(UserMixin, db.Model):
    __tablename__ = 'Permintaan_Service'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal_dibuat = db.Column(db.DateTime)
    npm = db.Column(db.Integer, ForeignKey('Mahasiswa'), nullable=False)
    id_kategori_konseling = db.Column(db.Integer, ForeignKey('Kategori_Konseling'), nullable=False)
    id_status_konseling = db.Column(db.Integer, ForeignKey('Status_Konseling'), nullable=False)
    id_pembatalan = db.Column(db.Integer, ForeignKey('Pembatalan'), nullable=True)
    id_room_meeting = db.Column(db.Integer, ForeignKey('Room_Meeting'), nullable=True)


class PermintaanJadwalService(UserMixin, db.Model):
    __tablename__ = 'Permintaan_Jadwal_Service'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal_pilih_service = db.Column(db.DateTime)
    id_jadwal_mingguan_konselor = db.Column(db.Integer, ForeignKey('Jadwal_Mingguan_Service'), nullable=False)
    id_permintaan_service = db.Column(db.Integer, ForeignKey('Permintaan_Service'), nullable=False)


class KategoriKonseling(UserMixin, db.Model):
    __tablename__ = 'Kategori_Konseling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(64))
    level = db.Column(db.Integer)


class HasilKonseling(UserMixin, db.Model):
    __tablename__ = 'Hasil_Konseling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    penyebab = db.Column(db.Text)
    solusi = db.Column(db.Text)
    tambahan = db.Column(db.Text)


class ServiceKonseling(UserMixin, db.Model):
    __tablename__ = 'Service_Konseling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_permintaan_service = db.Column(db.Integer, ForeignKey('Permintaan_Service'), nullable=False)
    id_kategori_konseling = db.Column(db.Integer, ForeignKey('Kategori_Konseling'), nullable=False)
    id_hasil_konseling = db.Column(db.Integer, ForeignKey('Hasil_Konseling'), nullable=True)


class Object_EPPS(UserMixin, db.Model):
    __tablename__ = 'Object_EPPS'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    penerbit = db.Column(db.String(124), nullable=False)
    pembuat = db.Column(db.String(124), nullable=False)
    tahun_terbit = db.Column(db.Integer, nullable=False)


class Interpretasi_EPPS(UserMixin, db.Model):
    __tablename__ = 'Interpretasi_EPPS'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    achievement = db.Column(db.Text, nullable=False)
    deference = db.Column(db.Text, nullable=False)
    order = db.Column(db.Text, nullable=False)
    exhibition = db.Column(db.Text, nullable=False)
    autonomy = db.Column(db.Text, nullable=False)
    affiliation = db.Column(db.Text, nullable=False)
    intraception = db.Column(db.Text, nullable=False)
    succorance = db.Column(db.Text, nullable=False)
    dominance = db.Column(db.Text, nullable=False)
    abasement = db.Column(db.Text, nullable=False)
    Nurturance = db.Column(db.Text, nullable=False)
    change = db.Column(db.Text, nullable=False)
    endurance = db.Column(db.Text, nullable=False)
    heterosexuality = db.Column(db.Text, nullable=False)
    aggression = db.Column(db.Text, nullable=False)


class ServiceEPPS(UserMixin, db.Model):
    __tablename__ = 'Service_EPPS'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_permintaan_service = db.Column(db.Integer, ForeignKey('Permintaan_Service'), nullable=False)
    id_object_epps = db.Column(db.Integer, ForeignKey('Object_EPPS'), nullable=False)
    id_interpretasi_epps = db.Column(db.Integer, ForeignKey('Interpretasi_EPPS'), nullable=False)


class PertanyaanEPPS(UserMixin, db.Model):
    __tablename__ = 'Pertanyaan_EPPS'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_objek_epps = db.Column(db.Integer, ForeignKey('Object_EPPS'), nullable=False)
    pertanyaan = db.Column(db.Text, nullable=False)
    jawaban_a = db.Column(db.Text, nullable=False)
    jawaban_b = db.Column(db.Text, nullable=False)


class SkorEPPS(UserMixin, db.Model):
    __tablename__ = 'Skor_EPPS'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_service_epps = db.Column(db.Integer, ForeignKey('Service_EPPS'), nullable=False)
    kebutuhan = db.Column(db.Enum('Ach','Def','Ord','Exh','Aut','Aff','Int','Suc','Dom','Aba','Nur','Chg','End','Hef','Agg'), nullable=False)
    baris = db.Column(db.Integer, nullable=False)
    kolom = db.Column(db.Integer, nullable=False)
    jumlah = db.Column(db.Integer, nullable=False)
    skor_skalar = db.Column(db.Float, nullable=False)


class SystemSession(UserMixin):
    def __init__(self, nomer_id, nama_lengkap, nama_panggilan, jenis_kelamin, tanggal_lahir, user_type, id_status, info_tambahan={}, active=True):
        self.nomer_id = nomer_id
        self.nama_lengkap = nama_lengkap
        self.nama_panggilan = nama_panggilan
        self.jenis_kelamin = jenis_kelamin
        self.tanggal_lahir = tanggal_lahir
        self.user_type = user_type
        self.id_status = id_status
        self.info_tambahan = info_tambahan
        self.active = active

    def is_active(self):
        return self.active