# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rejish@1@localhost/python_database'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50))
#     middle_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     email = db.Column(db.String(120), unique=True)
#     phone_number = db.Column(db.String(20))
#     password = db.Column(db.String(80))
#     referral_code = db.Column(db.String(20))
#     promo_code = db.Column(db.String(20))
#     country = db.Column(db.String(50))
#     address_line1 = db.Column(db.String(120))
#     apartment_unit = db.Column(db.String(50))
#     city = db.Column(db.String(50))
#     state = db.Column(db.String(50))
#     zip_code = db.Column(db.String(20))

# @app.route('/', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         new_user = User(
#             first_name=request.form.get('first_name'),
#             middle_name=request.form.get('middle_name'),
#             last_name=request.form.get('last_name'),
#             email=request.form.get('email'),
#             phone_number=request.form.get('phone_number'),
#             password=request.form.get('password'),
#             referral_code=request.form.get('referral_code'),
#             promo_code=request.form.get('promo_code'),
#             country=request.form.get('country'),
#             address_line1=request.form.get('address_line1'),
#             apartment_unit=request.form.get('apartment_unit'),
#             city=request.form.get('city'),
#             state=request.form.get('state'),
#             zip_code=request.form.get('zip_code')
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         return 'Registration successful!'
#     return render_template('register.html')

# if __name__ == '__main__':
#     app.run(debug=True)
