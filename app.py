#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:


import openai
import os
from flask import Flask,render_template,request 
import replicate
openai.api_key='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'
os.environ["REPLICATE_API_TOKEN"]='r8_9SavgSCSZhOvF581nDUUGoRLetvXSHf1n0Peh'
m = replicate.models.get("tstramer/midjourney-diffusion")
version = m.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q=request.form.get("question")
        i={"prompt":q}
        r=version.predict(**i)
        return render_template("index.html",result=r[0])
    else:
        return(render_template('index.html',result='waiting..........'))
if __name__ =="__main__":
    app.run()


# In[ ]:


os.environ["REPLICATE_API_TOKEN"]='r8_9SavgSCSZhOvF581nDUUGoRLetvXSHf1n0Peh'
m = replicate.models.get("tstramer/midjourney-diffusion")
version = m.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")
