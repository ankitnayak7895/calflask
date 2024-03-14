from flask import Flask,request,render_template



obj=Flask(__name__)

@obj.route('/')
def home():
      return "<h>WELCOME TO THE FLASK HOME PAGE</h>"

@obj.route('/calculator',methods=['GET'])
def math():
      operation=request.json['opeartion']
      number1=request.json['number1']
      number2=request.json['number2']
      
      
      if operation=='add':
            result=number1+number2
      elif operation=='subtract':
            result=number1-number2
      elif operation=='multiply':
            result=number1*number2
            
      else:
            result=number1/number2
            
      return result
      
      
      
if __name__=="__main__":
      obj.run()