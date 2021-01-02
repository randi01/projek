from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class mahasiswaF(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama= StringField('Nama', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    kelas= StringField('Kelas', validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass=PasswordField('konfirmasi password', validators=[DataRequired(), EqualTo('password')])
    alamat= TextAreaField('Alamat')
    submit= SubmitField('Tambah')

    #cek npm
    def validate_npm(self, npm):
        ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM Yang Lain')

 #cek email
    def validate_email(self, email):
        cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('Email Sudah Terdaftar, Gunakan Email Yang Lain')
class loginmahasiswaF(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired()])
    submit= SubmitField('Login')

class editmahasiswaF(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama= StringField('Nama', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    kelas= StringField('Kelas', validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass=PasswordField('konfirmasi password', validators=[DataRequired(), EqualTo('password')])
    alamat= TextAreaField('Alamat')
    foto= FileField('Ubah Foto Profil', validators=[FileAllowed(['jpg','png'])])
    submit= SubmitField('Ubah Data')

    #cek npm
    def validate_npm(self, npm):
        if npm.data != current_user.npm:
            ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM Yang Lain')

    #cek email
    def validate_email(self, email):
        if email.data != current_user.email:
            cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError('Email Sudah Terdaftar, Gunakan Email Yang Lain')

class pengaduanF(FlaskForm):
    subjek= StringField('Subjek', validators=[DataRequired()])
    kategori= SelectField(u'kategori pengaduan', choices=[('administrasi','Pelayanan administrasi'), ('fasilitas','Fasilitas'), ('dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan= TextAreaField('pengaduan', validators=[DataRequired()])
    submit= SubmitField('kirim')