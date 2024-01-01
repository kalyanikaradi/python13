#!/usr/bin/env python
# coding: utf-8

# In[1]:


#inheritance(allow us to define class that inherits all methods and properties from another class)
#addition
class parent:
    def disp_a(self):
        self.a=int(input("enter a"))
        print("a" ,self.a)


# In[2]:


class child(parent):
    def disp_b(self):
        self.b=int(input("enter b"))
        print("b" ,self.b)
    def add(self):
        print(self.a+self.b)


# In[3]:


obj=child()
obj.disp_a()
obj.disp_b()
obj.add()


# In[4]:


class parent:
    def disp_a(self):
        self.a=int(input("enter a"))
        print("a" ,self.a)


# In[5]:


class child(parent):
    def disp_b(self):
        self.b=int(input("enter b"))
        print("b" ,self.b)
    def sub(self):
        print(self.a-self.b)


# In[6]:


ob=child()
ob.disp_a()
ob.disp_b()
ob.sub()


# In[10]:


#multiplication
class parent:
      def disp_a(self):
            self.a=int(input("enter a"))
            print("a" ,self.a)


# In[12]:


class child(parent):
    def disp_b(self):
        self.b=int(input("enter b"))
        print("b" ,self.b)
    def mul(self):
        print(self.a*self.b)


# In[13]:


ob=child()
ob.disp_a()
ob.disp_b()
ob.mul()


# In[17]:


#division
class parent:
    def disp_a(self):
        self.a=int(input("enter a"))
        print("a" ,self.a)


# In[18]:


class child(parent):
    def disp_b(self):
        self.b=int(input("enter b"))
        print("b" ,self.b)
    def div(self):
        print(self.a/self.b)


# In[19]:


obj=child()
obj.disp_a()
obj.disp_b()
obj.div()


# In[ ]:




