import streamlit as st

def main():
    st.title("Hello ryfai users!")
    st.markdown("Thank you for choosing private AI!")
    st.markdown("This is how to use the RYFAI app!")
    st.write("_____________________________________________________________")
    if st.button("Buttons and Widgets"):
        st.markdown("**Model output widget**: The top of the app is a text area where you will see the AI's responses to your questions.\n"
                    "It is not editable. Do not worry if responses do not show up right away, I am still working on streaming responses")
        st.markdown("**Text input widget**: Below the model output widget is an area where you can write your questions. You can paste code in there and ask very long questions")
        st.markdown("**Ask button**: Trigger to ask the model what questions you put in the text input widget")
        st.markdown("**Dropdown widget to the right**: This widget, when clicked, allows you to choose which AI model you are using.\n"
                    "If you click on an AI model you dont have installed, RYFAI will ask you if you want to install the model before use")
        st.markdown("**Save as PNG and save as text**: Save as PNG takes a screenshot of your chat, and saves it to a file called 'chat.png' in the folder of the program\n"
                    "The same thing goes for 'Save as text' where instead of an image, it saves the conversation as a text file")
        st.markdown("**How to use button**: Takes you to this page!")
        st.markdown("**About button**: Displays information about RYFAI")
        st.markdown("**Donate button**: Click this to donate to me! Simply enter your info that is asked for, and donate as much as you like to the RYFAI project.")
    st.write("__________________________________________________________________")
    if st.button("Download RYFAI for yourself!"):
        st.markdown("Currently not open source, but email ryfai@proton.me if you are interested in being a part of the developer team")
        st.markdown("FOR EVERYONE ELSE: https://github.com/PetertheRedCedar/ryfai/releases")
    st.write("_____________________________________________________________")
    if st.button("Why RYFAI?"):
        st.markdown("There are major problems in the tech world regarding a user's privacy, especially in AI. Giant corporations love to gather your data\n"
                    "and give it to advertisers to sell you an ad using your personal conversation data, or they use your conversation data to train these\n"
                    "massive AI systems they have built. These companies have built remarkable products, but with great power comes great responsibility, and they\n"
                    "have seemed to abuse that power quite a lot!\n"
                    "\n"
                    "This is why I created RYFAI. RYFAI is like all of these great products these companies have made, but it is free and comes with the USERS in\n"
                    "mind, not the profit. You can ensure RYFAI does not take your data because you can use RYFAI without being connected to the internet (and you\n"
                    "can also look at the code yourself)! RYFAI not only leverages the power of AI, but it also comes with the PEOPLE in mind, over the profit.\n"
                    "With those two things combined, you have an unbeatable product. Now THATS remarkable!")

if __name__ == "__main__":
    main()
