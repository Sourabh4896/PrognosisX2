import streamlit as st

def main():
    st.title("Model training ")

    # Dropdown to select a model name
    model_names = [
       "Xception",
        "VGG16",
        "VGG19",
        "ResNet50",
        "ResNet50V2",
        "ResNet101",
        "ResNet101V2",
        "ResNet152",
        "ResNet152V2",
        "InceptionV3",
        "InceptionResNetV2",
        "MobileNet",
        "MobileNetV2",
        "DenseNet121",
        "DenseNet169",
        "DenseNet201",
        "NewModel"  # Added new model
    ]

    selected_model = st.selectbox("Select Model ", model_names)

    # st.subheader("Total category")

    sel_class = st.number_input("Total category", value=0,format="%d")
    class_list = []
    for i in range(sel_class):
        class_name = "class_" + str(i+1)
        val = st.text_input(class_name, 'Folder path')
        class_list.append(val)
        
    # Input sections for three numbers
    number1 = st.number_input("Data repitation", value=0, step=1, format="%d")
    number2 = st.number_input("image size", value=0, step=1, format="%d")
    number3 = st.number_input("Total devision of dataset", value=0, step=1, format="%d")

  
        

    # Submit button
    if st.button("Submit"):
        # Process the data when the button is clicked
        st.write("Selected Model:", selected_model)
        st.write("Entered Numbers:")
        st.write("Epochs:", number1)
        st.write("image size", number2)
        st.write("Batch size", number3)

if __name__ == "__main__":
    main()