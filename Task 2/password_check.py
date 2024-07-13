import streamlit as st
import re 
from zxcvbn import zxcvbn



def check(password):
    results = zxcvbn(password)

    print(results)
    if len(password)<5:
        return 0,'Very Weak','red'
    if len (password)>=5 and len (password)<7:
        if re.search(r'[A-Za-z0-9]', password) or re.search(r'[^A-Za-z0-9]', password):
            if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password): 

                if re.search(r'[0-9]',password):

                    if  re.search(r'[^A-Za-z0-9]', password):

                        strength = 'Strong'
                        strength_color = 'green'
                        return 80 , strength, strength_color
                    else:
                        strength = 'Medium'
                        strength_color = 'orange'
                        return 60 , strength, strength_color
                else:
                        strength = 'Medium'
                        strength_color = 'orange'
                        return 55 , strength, strength_color
            else:
                    
                    strength = 'Weak'
                    strength_color = 'red'
                    return 20 , strength, strength_color
            
        else:
              strength = 'Weak'
              strength_color = 'red'
              return 20 , strength, strength_color
            
        return 10 , 'Weak' , 'red'
    


    if len (password)>=7 and len(password)<9 :
        if re.search(r'[A-Za-z0-9]', password) or re.search(r'[^A-Za-z0-9]', password):
            if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password): 

                if re.search(r'[0-9]',password):

                    if  re.search(r'[^A-Za-z0-9]', password):

                        strength = 'Very Strong'
                        strength_color = 'green'
                        return 100 , strength, strength_color
                    else:
                        strength = 'Medium'
                        strength_color = 'orange'
                        return 80 , strength, strength_color
                else:
                        strength = 'Medium'
                        strength_color = 'orange'
                        return 60 , strength, strength_color
            else:
                    
                    strength = 'Weak'
                    strength_color = 'red'
                    return 40 , strength, strength_color
            
        else:
              strength = 'Weak'
              strength_color = 'red'
              return 30 , strength, strength_color
    if len(password)>=9:
                        strength = 'Very Strong'
                        strength_color = 'green'
                        return 100 , strength, strength_color
         



def main ():
    st.title("password Strength Checker")


    password = st.text_input("Enter your Password",type='password')


    if password:
        progress, strength , color = check(password)
        st.write(f"password Strength : {strength}")

        bar_html =f"""
        <div style='width: 100%; background-color: #ddd;'>
            <div style='width: {progress}%; height: 20px; background-color: {color};'></div>
        </div>
        """
        
        st.markdown(bar_html,unsafe_allow_html=True)
        if strength == 'Very Weak':
                st.error("Your password is very weak. Consider making it longer and adding numbers, uppercase letters, and special characters.")
        elif strength == 'Weak':
                st.warning("Your password is weak. Consider adding more numbers, uppercase letters, and special characters.")
        elif strength == 'Medium':
                st.info("Your password is of medium strength. You can make it stronger by adding special characters.")
        elif strength == 'Strong':
                st.success("Your password is strong. For maximum security, consider  adding more characters.")
        elif strength == 'Very Strong':
                st.balloons()
                st.success("Your password is very strong! Great job!")

if __name__ == '__main__':
    main()
