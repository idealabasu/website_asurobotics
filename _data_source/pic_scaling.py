# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:46:31 2017

@author: daukes
"""

from PIL import Image
import os
import glob

def crop(subdir,goal_ratio,basewidth,crop):
    
    files = []
    
    src_dir='../_assets_src/'+subdir
    final_dir='../assets/'+subdir
    files.extend(glob.glob(src_dir+'/*.jpg'))
    files.extend(glob.glob(src_dir+'/*.png'))
    files.extend(glob.glob(src_dir+'/*.gif'))
    
    def crop_center(img,w,h):
        x = img.width/2
        y = img.height/2
        img = img.crop((x-w/2,y-h/2,x+w/2,y+h/2))
        return img
    
    if not os.path.exists('mod'):
        os.mkdir('mod')
    
    goal_ratio_r = round(goal_ratio,3)
    
    
    if not os.path.exists(final_dir):
        os.mkdir(final_dir)
    for filename in files:
        print(filename)
        img = Image.open(filename)
        b = os.path.split(filename)
    
        if crop:    
            actual_ratio = img.width/img.height
            actual_ratio_r = round(actual_ratio,3)
            
            if actual_ratio_r > goal_ratio_r:
                print('reduce width')
                h = img.height
                w = img.height*goal_ratio
                img = crop_center(img,w,h)
            
            elif actual_ratio_r < goal_ratio_r:
                print('reduce height')
                w = img.width
                h = img.width/goal_ratio
                img = crop_center(img,w,h)
        
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img2 = img.resize((basewidth, hsize), Image.ANTIALIAS)
        newfilename = os.path.join(final_dir,b[1])
        #print(newfilename)
        img2.save(newfilename,quality=80)

crop('headshots',5/7,400,True)
crop('labs',7/5,400,False)
crop('carousels/homepage',7/5,1000,True)
crop('carousels/startup-lab',7/5,1000,True)