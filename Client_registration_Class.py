from datetime import date
from random import randrange
import os

class Client():
    def __init(self, id, Name, Cpf, Birth_Date_day, Birth_Date_month, Birth_Date_year, Gender, Road, Number, CEP, District, State, phone_country_code, phone_ddd, phone_number):
        self.client_id = id
        self.client_name = str(Name.upper())
        self.client_birth_date = date(Birth_Date_year, Birth_Date_month,Birth_Date_day)
        self.client_gender = Gender
        self.client_address = {"Hroad":Road,"Hnumber":Number, "Hcep":CEP, "Hdistrict":District, "Hstate":State}
        self.client_phone_num = {"country_code": phone_country_code, "ddd": phone_ddd, "num":phone_number}
    
    def CpfAutentication(self):
        if len(self.client_cpf) == 11:
            self.client_cpf = self.client_cpf.zfill(11)
            self.client_cpf = '{}.{}.{}-{}'.format(self.client_cpf[:3], self.client_cpf[3:6], self.client_cpf[6:9], self.client_cpf[9:])
            return True
        elif len(self.client_cpf) >= 10 or len(self.client_cpf) <= 12:
            print("this number is not a cpf")
            return False
        else:   
            self.client_cpf = '000.000.000-00'
            return False
    
    def GenUserId():
        gen_code_date = date.today()
        #encontrar outro meio para realizar a geração do id para que não tenha repetições que podem causar erros futuros
        client_id = '{}{}{}'.format(gen_code_date.year,gen_code_date.month,randrange(10000,99999))
        return client_id
    
    def GenClientDocumentFolder(self):
        directory_name_folder = self.client_id
        os.makedirs(f'./PersonalClientsFolder/{self.client_id}')