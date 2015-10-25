'''
Created on Oct 25, 2015
@author: Wuga
This code is modified from online article "How to make beautiful data visualizations in Python with matplotlib"
If there is anything unclear, please search this article online:
http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
'''
import matplotlib.pyplot as plt  
import pandas as pd  
import matplotlib.gridspec as gridspec
    
term_cvalue_data = pd.read_csv("csv/sample.csv")    
   
RGBcolors = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
    
for i in range(len(RGBcolors)):    
    r, g, b = RGBcolors[i]    
    RGBcolors[i] = (r / 255., g / 255., b / 255.)    
   
plt.figure(figsize=(10, 7.5))    
   
gs = gridspec.GridSpec(3, 2,
                       width_ratios=[10,1],
                       height_ratios=[1,20,1]
                       ) 
ax = plt.subplot(gs[2])    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)    
    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()    
   
plt.ylim(0, 90)    
plt.xlim(1990, 2004)    
      
plt.yticks(range(0, 91, 10), [str(x) for x in range(0, 91, 10)], fontsize=14)    
plt.xticks(fontsize=14)    
   
for y in range(10, 91, 10):    
    plt.plot(range(1990, 2003), [y] * len(range(1990, 2003)), "--", lw=0.5, color="black", alpha=0.3)    
     
plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on")    
  
majors=list(term_cvalue_data.columns.values)
  
for rank, column in enumerate(majors):       
    plt.plot(term_cvalue_data.Year.values,    
            term_cvalue_data[column.replace("\n", " ")].values,    
            lw=2.5, color=RGBcolors[rank])    
    
    y_pos = term_cvalue_data[column.replace("\n", " ")].values[-1] - 0.5    
    if column == "nervous system":    
        y_pos -= 1.5    
    elif column == "research project":    
        y_pos -= 0.75    

    plt.text(2003.5, y_pos, column, fontsize=14, color=RGBcolors[rank])    
    
plt.text(1997, 93, "Term frequency of NSF Dataset"    
       ", From 1990-2003", fontsize=17, ha="center")    
  
plt.savefig("term_frequancy_curve.png", bbox_inches="tight")  
plt.show()