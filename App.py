import streamlit as st
import pandas as pd
import base64
import webbrowser
import time





nav = st.sidebar.radio("Select",["Youtube","Facebook","About Us"])


    

if nav == "Youtube":
   
    
    title,img =st.columns([2,1])
    with title :
        st.title("Welcome to Chhanel")
    with img:
        st.image("youtube.png")
        


    logo,text= st.columns([1,2])
    
    with logo:
        st.image("logo.png")
    with text :
        
        st.markdown("# **Bhakti With Nisha** 	:sparkles: ",True)
        st.markdown('## Yt Handel 	   :arrow_forward:   @tv009')
    head,subs = st.columns([2,1])
    
    with head:
     st.markdown(" ### SUBSCRIBE THE CHANNEL")
    with subs:
        url ='https://www.youtube.com/@tv009'
        if st.button(("SUBSCRIBE")): 
          webbrowser.open_new_tab(url)
    st.markdown("## Top-Songs    :arrow_forward:")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://www.youtube.com/watch?v=lGkMkYC4MXA")
    with song2:
        st.video("https://www.youtube.com/watch?v=38ATgNTI8HE")


    st.markdown("## Bhajans    :arrow_forward:")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://www.youtube.com/watch?v=pSUziDYApv4&list=PLSLAQUhCKen3ZQGPEypSbJqBWON7DrP0n&index=3")
    with song2:
        st.video("https://www.youtube.com/watch?v=I88gJKix3qM&list=PLSLAQUhCKen3ZQGPEypSbJqBWON7DrP0n&index=1")

    st.markdown("## Vastu-Tips    :arrow_forward:")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://www.youtube.com/watch?v=f5BHgYUTkD8&list=PLSLAQUhCKen3kZnHH1lcrFWVn-K26r8LW&index=4")
    with song2:
        st.video("https://www.youtube.com/watch?v=NyeUMCq_BTY&list=PLSLAQUhCKen3kZnHH1lcrFWVn-K26r8LW&index=5")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://youtu.be/UnAkdW-y7yk?si=6nnYNfNMUlLRu8xU")
    with song2:
        st.video("https://www.youtube.com/watch?v=NyeUMCq_BTY&list=PLSLAQUhCKen3kZnHH1lcrFWVn-K26r8LW&index=5")

    st.select_slider("Rating",["bad","good","best","excelent"])

    st.markdown(" # And Many More Things")
    visit,youtube = st.columns([4,1])
    with visit:
        st.markdown(""" **To Visit Our Youtube Channel**
                
                 """)
    with youtube:
        st.image("youtube.png")

    click,button = st.columns([2,4])
    with click:
        st.markdown(""" 
                _Click on the button_
                 """)
    with button:
        id ='https://www.youtube.com/@tv009'
        if st.button(("VISIT CHANNEL")): 
          webbrowser.open_new_tab(id)


    time.sleep(5)

    tt=st.balloons()
        

        
        

        



if nav == "Facebook":
    
    
    title,img =st.columns([2,1])
    with title :
        st.title("Welcome to Chhanel")
    with img:
        st.image("facebook.png",width=150)
        


    logo,text= st.columns([1,2])
    
    with logo:
        st.image("logo.png")
    with text :
        
        st.markdown("# **Bhakti With Nisha** 	:moon: ",True)
        st.markdown('## facebook Handel 	   :star:    @bhaktiwithnisha')
    head,subs = st.columns([2,1])
    
    with head:
     st.markdown(" ### FOLLOW THE CHANNEL")
    with subs:
        url ='https://www.facebook.com/profile.php?id=100094038468018'
        if st.button(("SUBSCRIBE")): 
          webbrowser.open_new_tab(url)
    st.markdown("## Top-Songs    :arrow_forward:")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://www.youtube.com/watch?v=lGkMkYC4MXA")
    with song2:
        st.video("https://www.youtube.com/watch?v=38ATgNTI8HE")


    st.markdown("## Bhajans    :arrow_forward:")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://www.youtube.com/watch?v=pSUziDYApv4&list=PLSLAQUhCKen3ZQGPEypSbJqBWON7DrP0n&index=3")
    with song2:
        st.video("https://www.youtube.com/watch?v=I88gJKix3qM&list=PLSLAQUhCKen3ZQGPEypSbJqBWON7DrP0n&index=1")

    st.markdown("## Vastu-Tips    :arrow_forward:")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://www.youtube.com/watch?v=f5BHgYUTkD8&list=PLSLAQUhCKen3kZnHH1lcrFWVn-K26r8LW&index=4")
    with song2:
        st.video("https://www.youtube.com/watch?v=NyeUMCq_BTY&list=PLSLAQUhCKen3kZnHH1lcrFWVn-K26r8LW&index=5")
    song1,song2 = st.columns([1,1])
    with song1:
        st.video("https://youtu.be/UnAkdW-y7yk?si=6nnYNfNMUlLRu8xU")
    with song2:
        st.video("https://www.youtube.com/watch?v=NyeUMCq_BTY&list=PLSLAQUhCKen3kZnHH1lcrFWVn-K26r8LW&index=5")
    
    st.select_slider("Rating",["bad","good","best","excelent"])

    
    st.markdown(" # And Many More Things")
    visit,youtube = st.columns([4,1])
    with visit:
        st.markdown(""" **To Visit Our Youtube Channel**
                
                 """)
    with youtube:
        st.image("youtube.png")

    click,button = st.columns([2,4])
    with click:
        st.markdown(""" 
                _Click on the button_
                 """)
    with button:
        id ='https://www.youtube.com/@tv009'
        if st.button(("VISIT CHANNEL")): 
          webbrowser.open_new_tab(id)


    time.sleep(5)

    tt=st.balloons()

if nav == "About Us":
    
    st.markdown("# <U> <B>     :star: About Us :star:  <b>",True)
    st.image("logo.png")
    st.subheader('''Welcome to The Bhakti With Nisha Channel, your search for peace & calmness ends here. Your one stop destination for all types of Bhajans, Kirtans, Mantras,Facts,Vastu Shastra Tips,Devotional Stories,Horoscope,Garuda Purana Tips,Informative Videos etc of all Hindu Gods for stress relief and improved quality of life. Subscribe to get Regular Updates from this Channel''')
    

    button1,button2=st.columns([1,2])
    with button1:
        id ='https://www.youtube.com/@tv009'
        if st.button(("Youtube")): 
          webbrowser.open_new_tab(id)
    with button2:
        id ='https://www.facebook.com/profile.php?id=100094038468018'
        if st.button(("Facebook")): 
          webbrowser.open_new_tab(id)

    st.title("For Bussiness Enquiry")
    my_form=st.form
    # creating input fields
    f,l=st.columns([1,1])
    with f :
        fname=st.text_input('First Name:')
    with l:
        lname=st.text_input('Last Name')

    email, mob =st.columns([3,2])
    with email:
        email.text_input('Email Id')
    with mob:
        mob.text_input('Mobile No')
    st.text_area("Description")
    st.file_uploader("file")
    st.button("Submit")
    time.sleep(5)

    tt=st.balloons()
    # user,pw,pw2=my_form.columns(3)
    # user.text_input("User Name")
    # pw.text_input("Password",type="password")
    # pw2.text_input("Re-Password",type="password")

    # ch,bl,sub = st.columns(3)
    # with ch:
    #     my_form.checkbox("I agree")
    # with sub:
    #     my_form.form_submit_button("SUBMIT")



# # creating input fields
# fname=my_form.text_input('First Name:')
# lname=my_form.text_input('Last Name')

# email, mob = my_form.columns([3,1])
# email.text_input('Email Id')
# mob.text_input('Mobile No')

# user,pw,pw2=my_form.columns(3)
# user.text_input("User Name")
# pw.text_input("Password",type="password")
# pw2.text_input("Re-Password",type="password")

# ch,bl,sub = st.columns(3)
# with ch:
#     my_form.checkbox("I agree")
# with sub:
#     my_form.form_submit_button("SUBMIT")
# # Multi Layout in Single line concept 
# # with col1:
# #     st.button('Button 1')
# # with col2:
# #     st.button('Button 2')
# # with col3:
# #     st.button('Button 3')
