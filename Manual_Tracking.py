import sys
import os
Importing = 0
if Importing ==0:
    '''
    try:
        os.system('cmd /c "python3 -m pip --version"')
    except:
        os.system('cmd /c "python -m ensurepip --default-pip --no-input"')
    else:
        pass
    '''
    try:
        import numpy
    except ImportError:
        #os.system('cmd /c "pip install os.path.join(os.environ['USERPROFILE'],"Downloads","Manual_Tracking","Numpy","numpy-1.19.5+vanilla-cp{}{}-cp{}{}-win_amd64.whl") --no-input"'.format(sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor))
        if sys.version_info.minor == 6 or sys.version_info.minor == 7:
            raise ImportError("Missing Numpy, please install the 64-bit version by downloading 'numpy-1.19.5+vanilla-cp{}{}-cp{}{}m-win_amd64.whl' from 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy'.  In command prompt, type 'cd Downloads', then install 64-bit numpy with 'pip install numpy-1.19.5+vanilla-cp{}{}-cp{}{}m-win_amd64-win_amd64.whl'.".format(sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor))
        if sys.version_info.minor == 8 or sys.version_info.minor == 9:
            raise ImportError("Missing Numpy, please install the 64-bit version by downloading 'numpy-1.19.5+vanilla-cp{}{}-cp{}{}-win_amd64.whl' from 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy'.  In command prompt, type 'cd Downloads', then install 64-bit numpy with 'pip install numpy-1.19.5+vanilla-cp{}{}-cp{}{}-win_amd64.whl'.".format(sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor))
         
    else:
        import numpy as np
        from numpy import logical_and
        import numpy.distutils.system_info as sysinfo
        if sysinfo.platform_bits != 64:
            #os.system('cmd /c "pip uninstall numpy --no-input"')
            #os.system('cmd /c "pip install os.path.join(os.environ['USERPROFILE'],"Downloads","Manual_Tracking","Numpy","numpy-1.19.5+vanilla-cp{}{}-cp{}{}-win_amd64.whl") --no-input"'.format(sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor))
            if sys.version_info.minor == 6 or sys.version_info.minor == 7:
                raise ImportError("Missing 64-bit Numpy, please install the 64-bit version by downloading 'numpy-1.19.5+vanilla-cp{}{}-cp{}{}m-win_amd64.whl' from 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy'.  In command prompt, type 'cd Downloads', first uninstall the current 32-bit version with 'pip uninstall numpy', then install 64-bit numpy with 'pip install numpy-1.19.5+vanilla-cp{}{}-cp{}{}m-win_amd64.whl'.".format(sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor))
            if sys.version_info.minor == 8 or sys.version_info.minor == 9:
                raise ImportError("Missing 64-bit Numpy, please install the 64-bit version by downloading 'numpy-1.19.5+vanilla-cp{}{}-cp{}{}-win_amd64.whl' from 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy'.  In command prompt, type 'cd Downloads', first uninstall the current 32-bit version with 'pip uninstall numpy', then install 64-bit numpy with 'pip install numpy-1.19.5+vanilla-cp{}{}-cp{}{}-win_amd64.whl'.".format(sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor,sys.version_info.major,sys.version_info.minor))
            
        
    try:
        import skimage
    except ImportError:
        #os.system('cmd /c "pip install scikit-image --no-input"')
        raise ImportError("Missing skimage, install with 'pip install scikit-image'")
    else:
        from skimage import io,color

    try:
        import tkinter
    except ImportError:
        raise ImportError("Missing tkinter, install from 'https://tkdocs.com/tutorial/install.html'")
    else:
        from tkinter import *
        from tkinter import messagebox, filedialog

    try:
        import matplotlib
    except ImportError:
        #os.system('cmd /c "pip install matplotlib --no-input"')
        raise ImportError("Missing matplotlib, install with 'pip install matplotlib'")
    else:
        import matplotlib.pyplot as plt
        import matplotlib.colors as color
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        
    
    try:
        import openpyxl
    except ImportError:
        #os.system('cmd /c "pip install openpyxl --no-input"')
        raise ImportError("Missing openpyxl, install with 'pip install openpyxl'")
    else:
        import openpyxl
        from openpyxl import Workbook
    
    try:
        import string
    except ImportError:
        #os.system('cmd /c "pip install string --no-input"')
        raise ImportError("Missing string, install with 'pip install string'")
    else:
        import string
    
import timeit
from os import listdir
from os.path import isfile, join
import time


#Possibly have to install openpyxl and numpy (64-bit)

if __name__ == '__main__':        
    root = Tk()
    canvas1 = Canvas(root, width = 500, height = 3754, relief = 'raised')
    canvas1.pack(fill=BOTH, expand=YES)
    
    global time_displayed
    global Entry_Tracked
    
    
    
    def Organize_Folders():
        folderPath = Input_Directory_Text.get()+'/'
        File_Names = np.array([(f,float(f.name)) for f in os.scandir(folderPath)])
        global Ascending_Order
        Ascending_Order = File_Names[File_Names[:,1].argsort()]
        file_names_combined = np.zeros((len(Ascending_Order),len(listdir(Ascending_Order[0,0].path)))).astype(np.unicode_)
        Organized_Files = []
        for x in range(len(Ascending_Order)):
            onlyfiles = [onlyfiles for onlyfiles in listdir(Ascending_Order[x,0].path) if isfile(join(Ascending_Order[x,0],onlyfiles))]
            z_slice_time_stamp_names = np.array([onlyfiles[x].split('.') for x in range(len(onlyfiles))])
            file_names_combined[x] = np.array([z_slice_time_stamp_names[z_slice_time_stamp_names[:,0].astype(np.float).argsort()][x][0]+'.'+z_slice_time_stamp_names[z_slice_time_stamp_names[:,0].astype(np.float).argsort()][x][1] for x in range(len(onlyfiles))])
            
        for x in range(len(file_names_combined[:,0])):
            for y in range(len(file_names_combined[0,:])):
                Organized_Files.append(Ascending_Order[x,0].path+'/'+str(file_names_combined[x,y]))
        Organized_Files = np.array(Organized_Files).reshape((len(file_names_combined[:,0]),len(file_names_combined[0,:])))
        
        #time_display_final_value.set(Organized_Files.shape[1])
        return Organized_Files
        
    class Contrast_Drawing(object):
        def __init__(self,fig,ax,hologram_min,hologram_max,Distribution_min,Distribution_max,hologram_mean,hologram_std):
            self.fig = fig
            self.ax = ax
            self.hologram_min = hologram_min
            self.hologram_max = hologram_max
            self.Distribution_min = Distribution_min
            self.Distribution_max = Distribution_max
            self.lower_contrast = hologram_mean-2*hologram_std
            self.upper_contrast = hologram_mean+2*hologram_std
            
            if self.hologram_min > self.lower_contrast:
                self.lower_contrast = self.hologram_min
            if self.hologram_max < self.lower_contrast:
                self.lower_contrast = self.hologram_max
            if self.hologram_min > self.upper_contrast:
                self.upper_contrast = self.hologram_min
            if self.hologram_max < self.upper_contrast:
                self.upper_contrast = self.hologram_max
            
            self.Contrast_Drawn_Lines =  plt.plot([self.lower_contrast,self.upper_contrast],[self.Distribution_min,self.Distribution_max],color='green')
            
            
        
        def update_contrast(self,*args):
            #if Initiated_Contrast_Check.get() == 1:
            print('adjusting line')
            print(f'Lower: {Lower_Contrast_Value.get()}, Upper: {Upper_Contrast_Value.get()}')
            print(f'Lower: {Lower_Contrast_Slider.get()}, Upper: {Upper_Contrast_Slider.get()}')
            self.line_removed = self.Contrast_Drawn_Lines.pop(0)
            self.line_removed.remove()
            del self.line_removed
            self.lower_contrast = Lower_Contrast_Value.get()
            self.upper_contrast = Upper_Contrast_Value.get()
            if self.hologram_min > self.lower_contrast:
                self.lower_contrast = self.hologram_min
            if self.hologram_max < self.lower_contrast:
                self.lower_contrast = self.hologram_max
            if self.hologram_min > self.upper_contrast:
                self.upper_contrast = self.hologram_min
            if self.hologram_max < self.upper_contrast:
                self.upper_contrast = self.hologram_max
            if self.lower_contrast > self.upper_contrast:
                self.temp = self.upper_contrast
                self.upper_contrast = self.lower_contrast
                self.lower_contrast = self.temp
                
            self.Contrast_Drawn_Lines =  plt.plot([self.lower_contrast,self.upper_contrast],[self.Distribution_min,self.Distribution_max],color='green')
            self.fig.canvas.draw_idle()
                
    class IndexTracker(object):
        def __init__(self, ax, X,Folder_Z_Values,time_displayed,Entry_Tracked):
            self.ax = ax
            self.start = -1 #Index of z-slice
            self.Z_Slice = Folder_Z_Values #The z values
            self.end_time = len(self.Z_Slice)
            ax.set_title('Navigation: Scroll wheel for Z and left/right for time')
            self.time_displayed = time_displayed
            global time_seen
            time_seen = self.time_displayed
            self.Entry_Tracker = Entry_Tracked

            self.X = X
            self.time_index, self.rows, self.cols, self.slices = X.shape
            self.ind = self.start
            global Z_Slice_Present
            Z_Slice_Present = int(self.Z_Slice[self.ind])
            
            self.Default_Contrast = 2
            self.im = ax.imshow(self.X[self.time_displayed,:, :, self.ind],cmap='gray')
            self.scrolled = 0
            self.shift_is_held = False
            self.control_is_held = False
            self.extent = [0,self.rows,0,self.cols]
            self.extent_temp = []
            self.lower_contrast = 0
            self.upper_contrast = 0
            self.update()

        def onscroll(self, event):
            if event.button == 'up':
                self.ind = (self.ind - 1) % self.slices
            else:
                self.ind = (self.ind + 1) % self.slices
            self.scrolled = 1
            self.update()
            
        def time_swap(self,event):
            if event.key == 'shift' or event.key == 'control':
                if event.key == 'shift' and self.shift_is_held == False:
                    self.shift_is_held = True
                if event.key == 'control' and self.control_is_held == False:
                    self.control_is_held = True
                
            if event.key == 'left' or event.key == 'right':
                if event.key == 'left':
                    self.time_displayed = (self.time_displayed-1) % self.time_index
                    self.Entry_Tracker = (self.Entry_Tracker-1) % 5
                if event.key == 'right':
                    self.time_displayed = (self.time_displayed+1) % self.time_index
                    self.Entry_Tracker = (self.Entry_Tracker+1) % 5
                global time_seen
                time_seen = self.time_displayed
                global Entry_Tracked
                Entry_Tracked = self.Entry_Tracker
                self.update()
        
        def on_key_release(self,event):
            if event.key == 'shift' or event.key == 'control':
                if event.key == 'shift' and self.shift_is_held == True:
                        self.shift_is_held = False
                if event.key == 'control' and self.control_is_held == True:
                        self.control_is_held = False
        
        def onclick(self,event):
            if event.xdata != None and event.ydata != None:
                if self.shift_is_held == True and event.button == 3:
                    self.extent = [0,self.rows,0,self.cols]
                    self.update()
                if self.control_is_held == True and event.button == 1:
                    self.extent_temp.append([event.xdata,event.ydata])
                    if len(self.extent_temp) == 2:
                        self.extent = [self.extent_temp[0][0],self.extent_temp[1][0],self.extent_temp[0][1],self.extent_temp[1][1]]
                        self.extent_temp = []
                        self.update()
                if self.shift_is_held == False and self.control_is_held == False:
                    X_Coordinate.set(np.floor(event.xdata))
                    Y_Coordinate.set(np.floor(event.ydata))
        
        def update(self):
            plt.axis(self.extent)
            global Z_Slice_Present
            Z_Slice_Present = int(self.Z_Slice[self.ind])
            global Index_Tracker
            Index_Tracker = self.ind
            
            
            if self.scrolled == 0:
                print(f'Checkbox: {Contrast_Button_Checkbox_value.get()}, Prior: {Contrast_Button_Checkbox_value_Prior.get()}, Contrast Button: {Contrast_Button_Check.get()}, Auto Contrast: {Auto_Contrast_Pressed.get()}')
                if Contrast_Button_Checkbox_value.get() == 0:
                    self.im.set_data(self.X[self.time_displayed,:, :, self.ind])
                if Contrast_Button_Checkbox_value_Prior.get() == 1:
                    self.im = ax.imshow(self.X[self.time_displayed,:,:,self.ind],cmap='gray')
                if Contrast_Button_Checkbox_value.get() == 1:
                    if Auto_Contrast_Pressed.get() == 1 or Contrast_Button_Check.get() == 1:
                        self.lower_contrast = Lower_Contrast_Value.get()
                        self.upper_contrast = Upper_Contrast_Value.get()
                        
                        if self.lower_contrast > self.upper_contrast:
                            self.temp = self.upper_contrast
                            self.upper_contrast = self.lower_contrast
                            self.lower_contrast = self.temp
                        self.im = ax.imshow(self.X[self.time_displayed,:,:,self.ind],vmin=self.lower_contrast,vmax=self.upper_contrast,cmap='gray')
                
                
                if Auto_Contrast_Pressed.get() == 1 and Contrast_Button_Checkbox_value.get() == 1:
                    self.lower_contrast = Lower_Contrast_Value.get()
                    self.upper_contrast = Upper_Contrast_Value.get()
                    self.im = ax.imshow(self.X[self.time_displayed,:,:,self.ind],vmin=self.lower_contrast,vmax=self.upper_contrast,cmap='gray')
            if self.scrolled == 1:
                self.im.set_data(self.X[self.time_displayed,:, :, self.ind])
            self.scrolled = 0
            ax.set_ylabel('time: %s, slice: %s' % (self.time_displayed+1,int(self.Z_Slice[self.ind])))
            self.im.axes.figure.canvas.draw_idle()
            Apply_Update_Notice_Label_Canvas = canvas1.create_window(650,open_window_spacing.get(),window=Apply_Update_Notice_Label)
            canvas1.delete(Apply_Update_Notice_Label_Canvas)

            
    def Finished():
        Enter_Time_Stamp_Data()
        File_To_Save = filedialog.asksaveasfile(mode='w',defaultextension='.xlsx')
        if File_To_Save is None:
            return
        if File_To_Save is not None:
            if File_To_Save.name[len(File_To_Save.name)-4:len(File_To_Save.name)] == 'xlsx':
                File = File_To_Save.name
            if File_To_Save.name[len(File_To_Save.name)-4:len(File_To_Save.name)] != 'xlsx':
                File = File_To_Save.name+'.xlsx'
                os.remove(File_To_Save.name)
        wb = Workbook()
        wb1 = wb.active
        wb.save(filename = File)
        for particle in range(int(Number_Of_Particles_To_Track.get())):
            if particle == 0:
                sheet = wb['Sheet']
                sheet.title = 'Particle #1'
            if particle != 0:
                sheet = wb.create_sheet('Particle #'+str(particle+1))
            sheet['A1'] = 'Time'
            sheet['B1'] = 'X'
            sheet['C1'] = 'Y'
            sheet['D1'] = 'Z'
            sheet['E1'] = 'Time Stamp'
            sheet['F1'] = 'Time Taken'
            sheet['G1'] = 'X Speed'
            sheet['H1'] = 'Y Speed'
            sheet['I1'] = 'Z Speed'
            sheet['J1'] = 'Total Speed'
            Alph = string.ascii_uppercase
            for x in range(int(int(Times_of_Interest.get()))):
                sheet['E'+str(2+x)] = Time_Stamp_Array_Times_of_Interest[x]
                if x > 0:
                    sheet['F'+str(2+x)] = np.round(sheet['E'+str(2+x)].value-sheet['E'+str(1+x)].value,5)
                for y in range(4):
                    sheet[Alph[y]+str(2+x)] = Particle_Locations[particle,x,y]
                if x > 0:
                    if Particle_Locations[particle,x,4] != 0 and Particle_Locations[particle,x-1,4] != 0:
                        sheet['G'+str(2+x)] = XY_Resolution_Variable.get()*(sheet['B'+str(2+x)].value - sheet['B'+str(1+x)].value)/sheet['F'+str(2+x)].value
                        sheet['H'+str(2+x)] = XY_Resolution_Variable.get()*(sheet['C'+str(2+x)].value - sheet['C'+str(1+x)].value)/sheet['F'+str(2+x)].value
                        sheet['I'+str(2+x)] = Z_Resolution_Variable.get()*(sheet['D'+str(2+x)].value - sheet['D'+str(1+x)].value)/sheet['F'+str(2+x)].value
                    
            dims = {}
            for row in sheet.rows:
                for cell in row:
                    if cell.value:
                        dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
            for col, value in dims.items():
                sheet.column_dimensions[col].width = value
                if value < len(sheet[col+'1'].value)+2:
                    sheet.column_dimensions[col].width = len(sheet[col+'1'].value)+2
                #if col == 'A':
                #    sheet.column_dimensions['A'].width = value+2
        wb.save(filename = File)
        wb.close()
    
    def Move_Page():
        Times_On_Pages_To_Display.set(int(int(int(Times_of_Interest.get()))-First_Time_Entry_Displayed.get()+1))
        
        
        gap = 28
        t_1.set(int(First_Time_Entry_Displayed.get()))
        t_2.set(int(First_Time_Entry_Displayed.get()+1))
        t_3.set(int(First_Time_Entry_Displayed.get()+2))
        t_4.set(int(First_Time_Entry_Displayed.get()+3))
        t_5.set(int(First_Time_Entry_Displayed.get()+4))
        x_1.set(int(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()-1,1]))
        y_1.set(int(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()-1,2]))
        z_1.set(int(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()-1,3]))
        if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()-1,4] == 1:
            t1_checked.set('Yes')
        if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()-1,4] == 0:
            t1_checked.set('No')
        
        t1_label_canvas = canvas1.create_window(50,entry1_spacing.get()*gap,window=t1_label)
        t1_entry_canvas = canvas1.create_window(75,entry1_spacing.get()*gap,window=t1_entry)
        x1_label_canvas = canvas1.create_window(95,entry1_spacing.get()*gap,window=x1_label)
        x1_entry_canvas = canvas1.create_window(125,entry1_spacing.get()*gap,window=x1_entry)
        y1_label_canvas = canvas1.create_window(155,entry1_spacing.get()*gap,window=y1_label)
        y1_entry_canvas = canvas1.create_window(185,entry1_spacing.get()*gap,window=y1_entry)
        z1_label_canvas = canvas1.create_window(215,entry1_spacing.get()*gap,window=z1_label)
        z1_entry_canvas = canvas1.create_window(245,entry1_spacing.get()*gap,window=z1_entry)
        t1checked_label_canvas = canvas1.create_window(295,entry1_spacing.get()*gap,window=t1checked_label)
        t1checked_entry_canvas = canvas1.create_window(345,entry1_spacing.get()*gap,window=t1checked_entry)
        t2_label_canvas = canvas1.create_window(50,entry2_spacing.get()*gap,window=t2_label)
        t2_entry_canvas = canvas1.create_window(75,entry2_spacing.get()*gap,window=t2_entry)
        x2_label_canvas = canvas1.create_window(95,entry2_spacing.get()*gap,window=x2_label)
        x2_entry_canvas = canvas1.create_window(125,entry2_spacing.get()*gap,window=x2_entry)
        y2_label_canvas = canvas1.create_window(155,entry2_spacing.get()*gap,window=y2_label)
        y2_entry_canvas = canvas1.create_window(185,entry2_spacing.get()*gap,window=y2_entry)
        z2_label_canvas = canvas1.create_window(215,entry2_spacing.get()*gap,window=z2_label)
        z2_entry_canvas = canvas1.create_window(245,entry2_spacing.get()*gap,window=z2_entry)
        t2checked_label_canvas = canvas1.create_window(295,entry2_spacing.get()*gap,window=t2checked_label)
        t2checked_entry_canvas = canvas1.create_window(345,entry2_spacing.get()*gap,window=t2checked_entry)
        t3_label_canvas = canvas1.create_window(50,entry3_spacing.get()*gap,window=t3_label)
        t3_entry_canvas = canvas1.create_window(75,entry3_spacing.get()*gap,window=t3_entry)
        x3_label_canvas = canvas1.create_window(95,entry3_spacing.get()*gap,window=x3_label)
        x3_entry_canvas = canvas1.create_window(125,entry3_spacing.get()*gap,window=x3_entry)
        y3_label_canvas = canvas1.create_window(155,entry3_spacing.get()*gap,window=y3_label)
        y3_entry_canvas = canvas1.create_window(185,entry3_spacing.get()*gap,window=y3_entry)
        z3_label_canvas = canvas1.create_window(215,entry3_spacing.get()*gap,window=z3_label)
        z3_entry_canvas = canvas1.create_window(245,entry3_spacing.get()*gap,window=z3_entry)
        t3checked_label_canvas = canvas1.create_window(295,entry3_spacing.get()*gap,window=t3checked_label)
        t3checked_entry_canvas = canvas1.create_window(345,entry3_spacing.get()*gap,window=t3checked_entry)
        t4_label_canvas = canvas1.create_window(50,entry4_spacing.get()*gap,window=t4_label)
        t4_entry_canvas = canvas1.create_window(75,entry4_spacing.get()*gap,window=t4_entry)
        x4_label_canvas = canvas1.create_window(95,entry4_spacing.get()*gap,window=x4_label)
        x4_entry_canvas = canvas1.create_window(125,entry4_spacing.get()*gap,window=x4_entry)
        y4_label_canvas = canvas1.create_window(155,entry4_spacing.get()*gap,window=y4_label)
        y4_entry_canvas = canvas1.create_window(185,entry4_spacing.get()*gap,window=y4_entry)
        z4_label_canvas = canvas1.create_window(215,entry4_spacing.get()*gap,window=z4_label)
        z4_entry_canvas = canvas1.create_window(245,entry4_spacing.get()*gap,window=z4_entry)
        t4checked_label_canvas = canvas1.create_window(295,entry4_spacing.get()*gap,window=t4checked_label)
        t4checked_entry_canvas = canvas1.create_window(345,entry4_spacing.get()*gap,window=t4checked_entry)
        t5_label_canvas = canvas1.create_window(50,entry5_spacing.get()*gap,window=t5_label)
        t5_entry_canvas = canvas1.create_window(75,entry5_spacing.get()*gap,window=t5_entry)
        x5_label_canvas = canvas1.create_window(95,entry5_spacing.get()*gap,window=x5_label)
        x5_entry_canvas = canvas1.create_window(125,entry5_spacing.get()*gap,window=x5_entry)
        y5_label_canvas = canvas1.create_window(155,entry5_spacing.get()*gap,window=y5_label)
        y5_entry_canvas = canvas1.create_window(185,entry5_spacing.get()*gap,window=y5_entry)
        z5_label_canvas = canvas1.create_window(215,entry5_spacing.get()*gap,window=z5_label)
        z5_entry_canvas = canvas1.create_window(245,entry5_spacing.get()*gap,window=z5_entry)
        t5checked_label_canvas = canvas1.create_window(295,entry5_spacing.get()*gap,window=t5checked_label)
        t5checked_entry_canvas = canvas1.create_window(345,entry5_spacing.get()*gap,window=t5checked_entry)
        canvas1.delete(t1_label_canvas)
        canvas1.delete(t1_entry_canvas)
        canvas1.delete(x1_label_canvas)
        canvas1.delete(x1_entry_canvas)
        canvas1.delete(y1_label_canvas)
        canvas1.delete(y1_entry_canvas)
        canvas1.delete(z1_label_canvas)
        canvas1.delete(z1_entry_canvas)
        canvas1.delete(t1checked_label_canvas)
        canvas1.delete(t1checked_entry_canvas)
        canvas1.delete(t2_label_canvas)
        canvas1.delete(t2_entry_canvas)
        canvas1.delete(x2_label_canvas)
        canvas1.delete(x2_entry_canvas)
        canvas1.delete(y2_label_canvas)
        canvas1.delete(y2_entry_canvas)
        canvas1.delete(z2_label_canvas)
        canvas1.delete(z2_entry_canvas)
        canvas1.delete(t2checked_label_canvas)
        canvas1.delete(t2checked_entry_canvas)
        canvas1.delete(t3_label_canvas)
        canvas1.delete(t3_entry_canvas)
        canvas1.delete(x3_label_canvas)
        canvas1.delete(x3_entry_canvas)
        canvas1.delete(y3_label_canvas)
        canvas1.delete(y3_entry_canvas)
        canvas1.delete(z3_label_canvas)
        canvas1.delete(z3_entry_canvas)
        canvas1.delete(t3checked_label_canvas)
        canvas1.delete(t3checked_entry_canvas)
        canvas1.delete(t4_label_canvas)
        canvas1.delete(t4_entry_canvas)
        canvas1.delete(x4_label_canvas)
        canvas1.delete(x4_entry_canvas)
        canvas1.delete(y4_label_canvas)
        canvas1.delete(y4_entry_canvas)
        canvas1.delete(z4_label_canvas)
        canvas1.delete(z4_entry_canvas)
        canvas1.delete(t4checked_label_canvas)
        canvas1.delete(t4checked_entry_canvas)
        canvas1.delete(t5_label_canvas)
        canvas1.delete(t5_entry_canvas)
        canvas1.delete(x5_label_canvas)
        canvas1.delete(x5_entry_canvas)
        canvas1.delete(y5_label_canvas)
        canvas1.delete(y5_entry_canvas)
        canvas1.delete(z5_label_canvas)
        canvas1.delete(z5_entry_canvas)
        canvas1.delete(t5checked_label_canvas)
        canvas1.delete(t5checked_entry_canvas)
        
        t1_label_canvas = canvas1.create_window(50,entry1_spacing.get()*gap,window=t1_label)
        t1_entry_canvas = canvas1.create_window(75,entry1_spacing.get()*gap,window=t1_entry)
        x1_label_canvas = canvas1.create_window(95,entry1_spacing.get()*gap,window=x1_label)
        x1_entry_canvas = canvas1.create_window(125,entry1_spacing.get()*gap,window=x1_entry)
        y1_label_canvas = canvas1.create_window(155,entry1_spacing.get()*gap,window=y1_label)
        y1_entry_canvas = canvas1.create_window(185,entry1_spacing.get()*gap,window=y1_entry)
        z1_label_canvas = canvas1.create_window(215,entry1_spacing.get()*gap,window=z1_label)
        z1_entry_canvas = canvas1.create_window(245,entry1_spacing.get()*gap,window=z1_entry)
        t1checked_label_canvas = canvas1.create_window(295,entry1_spacing.get()*gap,window=t1checked_label)
        t1checked_entry_canvas = canvas1.create_window(345,entry1_spacing.get()*gap,window=t1checked_entry)
        
        if Times_On_Pages_To_Display.get() > 1:
            t2_label_canvas = canvas1.create_window(50,entry2_spacing.get()*gap,window=t2_label)
            t2_entry_canvas = canvas1.create_window(75,entry2_spacing.get()*gap,window=t2_entry)
            x2_label_canvas = canvas1.create_window(95,entry2_spacing.get()*gap,window=x2_label)
            x2_entry_canvas = canvas1.create_window(125,entry2_spacing.get()*gap,window=x2_entry)
            y2_label_canvas = canvas1.create_window(155,entry2_spacing.get()*gap,window=y2_label)
            y2_entry_canvas = canvas1.create_window(185,entry2_spacing.get()*gap,window=y2_entry)
            z2_label_canvas = canvas1.create_window(215,entry2_spacing.get()*gap,window=z2_label)
            z2_entry_canvas = canvas1.create_window(245,entry2_spacing.get()*gap,window=z2_entry)
            t2checked_label_canvas = canvas1.create_window(295,entry2_spacing.get()*gap,window=t2checked_label)
            t2checked_entry_canvas = canvas1.create_window(345,entry2_spacing.get()*gap,window=t2checked_entry)
            x_2.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get(),1])
            y_2.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get(),2])
            z_2.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get(),3])
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get(),4] == 1:
                t2_checked.set('Yes')
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get(),4] == 0:
                t2_checked.set('No')
        if Times_On_Pages_To_Display.get()>2:
            t3_label_canvas = canvas1.create_window(50,entry3_spacing.get()*gap,window=t3_label)
            t3_entry_canvas = canvas1.create_window(75,entry3_spacing.get()*gap,window=t3_entry)
            x3_label_canvas = canvas1.create_window(95,entry3_spacing.get()*gap,window=x3_label)
            x3_entry_canvas = canvas1.create_window(125,entry3_spacing.get()*gap,window=x3_entry)
            y3_label_canvas = canvas1.create_window(155,entry3_spacing.get()*gap,window=y3_label)
            y3_entry_canvas = canvas1.create_window(185,entry3_spacing.get()*gap,window=y3_entry)
            z3_label_canvas = canvas1.create_window(215,entry3_spacing.get()*gap,window=z3_label)
            z3_entry_canvas = canvas1.create_window(245,entry3_spacing.get()*gap,window=z3_entry)
            t3checked_label_canvas = canvas1.create_window(295,entry3_spacing.get()*gap,window=t3checked_label)
            t3checked_entry_canvas = canvas1.create_window(345,entry3_spacing.get()*gap,window=t3checked_entry)
            x_3.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+1,1])
            y_3.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+1,2])
            z_3.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+1,3])
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+1,4] == 1:
                t3_checked.set('Yes')
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+1,4] == 0:
                t3_checked.set('No')
        if Times_On_Pages_To_Display.get() >3:
            t4_label_canvas = canvas1.create_window(50,entry4_spacing.get()*gap,window=t4_label)
            t4_entry_canvas = canvas1.create_window(75,entry4_spacing.get()*gap,window=t4_entry)
            x4_label_canvas = canvas1.create_window(95,entry4_spacing.get()*gap,window=x4_label)
            x4_entry_canvas = canvas1.create_window(125,entry4_spacing.get()*gap,window=x4_entry)
            y4_label_canvas = canvas1.create_window(155,entry4_spacing.get()*gap,window=y4_label)
            y4_entry_canvas = canvas1.create_window(185,entry4_spacing.get()*gap,window=y4_entry)
            z4_label_canvas = canvas1.create_window(215,entry4_spacing.get()*gap,window=z4_label)
            z4_entry_canvas = canvas1.create_window(245,entry4_spacing.get()*gap,window=z4_entry)
            t4checked_label_canvas = canvas1.create_window(295,entry4_spacing.get()*gap,window=t4checked_label)
            t4checked_entry_canvas = canvas1.create_window(345,entry4_spacing.get()*gap,window=t4checked_entry)
            x_4.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+2,1])
            y_4.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+2,2])
            z_4.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+2,3])
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+2,4] == 1:
                t4_checked.set('Yes')
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+2,4] == 0:
                t4_checked.set('No')
        if Times_On_Pages_To_Display.get() >4:
            t5_label_canvas = canvas1.create_window(50,entry5_spacing.get()*gap,window=t5_label)
            t5_entry_canvas = canvas1.create_window(75,entry5_spacing.get()*gap,window=t5_entry)
            x5_label_canvas = canvas1.create_window(95,entry5_spacing.get()*gap,window=x5_label)
            x5_entry_canvas = canvas1.create_window(125,entry5_spacing.get()*gap,window=x5_entry)
            y5_label_canvas = canvas1.create_window(155,entry5_spacing.get()*gap,window=y5_label)
            y5_entry_canvas = canvas1.create_window(185,entry5_spacing.get()*gap,window=y5_entry)
            z5_label_canvas = canvas1.create_window(215,entry5_spacing.get()*gap,window=z5_label)
            z5_entry_canvas = canvas1.create_window(245,entry5_spacing.get()*gap,window=z5_entry)
            t5checked_label_canvas = canvas1.create_window(295,entry5_spacing.get()*gap,window=t5checked_label)
            t5checked_entry_canvas = canvas1.create_window(345,entry5_spacing.get()*gap,window=t5checked_entry)
            x_5.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+3,1])
            y_5.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+3,2])
            z_5.set(Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+3,3])
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+3,4] == 1:
                t5_checked.set('Yes')
            if Particle_Locations[Particle_of_Focus.get(),First_Time_Entry_Displayed.get()+3,4] == 0:
                t5_checked.set('No')
        
        
    def Adjust_Particles_Tracked_Size(Temp_Array):
        global Particle_Locations
        Particle_Locations = np.zeros((int(Number_Of_Particles_To_Track.get()),Temp_Array.shape[1],Temp_Array.shape[2]),'<f4')
        Particle_Locations[:Temp_Array.shape[0],:,:] = np.copy(Temp_Array)
        Temp_Array = []
        Particle_Focus_Menu_Function()
    
    def Adjust_Particles_Tracked_Size_Warning():
        popup_warning = Tk()
        canvas_popup_warning = Canvas(popup_warning, relief = 'raised')
        canvas_popup_warning.pack(fill=BOTH, expand=YES)
        popup_warning.title("Warning")
        
        
        
        def Close_And_Finish():
            popup_warning.destroy()
            Finished()
            pass
        def Close():
            popup_warning.destroy()
            pass
        
        Warning_Label = Label(popup_warning,text='Number of particles tracked can not be lowered')
        Ok_Button = Button(popup_warning,text='Ok',command=Close,width=10)
        
        Warning_Label_Canvas = canvas_popup_warning.create_window(150,20,window=Warning_Label)
        Ok_Button_Canvas = canvas_popup_warning.create_window(150,48,window=Ok_Button)
        
        w = 300 # width for the Tk root
        h = 75 # height for the Tk root
        ws = popup_warning.winfo_screenwidth() # width of the screen
        hs = popup_warning.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        popup_warning.geometry('%dx%d+%d+%d' % (w, h, x, y))
        popup_warning.mainloop()
                
    def Adjust_Particles_Tracked_Size_Check(*args):
        if Window_Opened_Check.get() == 0:
            pass
        if Window_Opened_Check.get() == 1:
            if Number_Of_Particles_To_Track.get() != '':
                if Particle_Locations.shape[0] < int(Number_Of_Particles_To_Track.get()):
                    Temp_Array = np.copy(Particle_Locations)
                    Adjust_Particles_Tracked_Size(Temp_Array)
                if Particle_Locations.shape[0] > int(Number_Of_Particles_To_Track.get()):
                    Number_Of_Particles_To_Track.set(str(Particle_Locations.shape[0]))
                    Adjust_Particles_Tracked_Size_Warning()
                if Particle_Locations.shape[0] == int(Number_Of_Particles_To_Track.get()):
                    pass
                    
    def Particle_Focus_Menu_Function():
        article_Of_Focus_Label_Canvas = canvas1.create_window(450,y_input_spacing.get()*gap,window=Particle_Of_Focus_Label)
        Dic = {}
        for x in range(int(Number_Of_Particles_To_Track.get())):
            Dic[str(x+1)]=x+1
        Particle_Focus_Menu = OptionMenu(root,Particle_of_Focus_String,*Dic.keys())
        Particle_Focus_Menu_Canvas = canvas1.create_window(550,y_input_spacing.get()*gap,window=Particle_Focus_Menu)
    
    def Launch_Window():
        begin_timer = timeit.default_timer()
        Window_Opened_Check.set(1)
        Launched_Window.set(1)
        plt.close('all')
        global Phase_T,Phase_Z
        if Organized_Files_Done.get() == 0:
            if Derivative_Check_Variable.get() == 0:
                global Organized_Files
                Organized_Files = Organize_Folders()
                global shape_of_arrays_0,shape_of_arrays_1
                shape_of_arrays_0,shape_of_arrays_1 = np.array(io.imread(Organized_Files[0,0])).shape
                Phase_T = np.zeros((int(Times_of_Interest.get()),Organized_Files.shape[0],shape_of_arrays_0,shape_of_arrays_1),'<f4')
                Organized_Files_Done.set(1)
                for t_slice in range(int(Times_of_Interest.get())):
                    print(f'Building time slice #{t_slice+1} out of {int(Times_of_Interest.get())} ({np.round(timeit.default_timer() - begin_timer,3)} seconds)')
                    Phase_T_slice = np.zeros((Organized_Files.shape[0],shape_of_arrays_0,shape_of_arrays_1))
                    for z_slice in range(Organized_Files.shape[0]):
                        Phase_T_slice[z_slice,:,:] = np.array(io.imread(Organized_Files[z_slice,t_slice]),'<f4')*100
                    Phase_T[t_slice,:,:,:] = np.copy(Phase_T_slice)
            if Derivative_Check_Variable.get() == 1:
                Derivative_Image_Array = np.array(io.imread(Derivative_Input_File_Name.get()))
                Organized_Files_Done.set(1)
            
            created_list = 0
            if created_list == 0:
                created_list = 1
                global Particle_Locations
                Particle_Locations = np.zeros((int(Number_Of_Particles_To_Track.get()),int(Times_of_Interest.get()),5))
                Particle_Locations[:,:,0] = np.arange(int(Times_of_Interest.get()))+1
                
            display_show = True
            if display_show:
                Times_On_Pages_To_Display.set(int(int(Times_of_Interest.get())-First_Time_Entry_Displayed.get()+1))
                
                gap = 28
                
                if Times_On_Pages_To_Display.get()>5:
                    Left_Arrow_Button_Canvas = canvas1.create_window(100,arrows_jumping_spacing.get()*gap,window=Left_Arrow_Button)
                    Right_Arrow_Button_Canvas = canvas1.create_window(200,arrows_jumping_spacing.get()*gap,window=Right_Arrow_Button)
                
                    jump_to_label_canvas = canvas1.create_window(275,arrows_jumping_spacing.get()*gap,window=jump_to_label)
                    jump_to_entry_canvas = canvas1.create_window(345,arrows_jumping_spacing.get()*gap,window=jump_to_entry)
                if Times_On_Pages_To_Display.get()<6:
                    entry1_spacing.set(entry1_spacing.get()-1)
                    entry2_spacing.set(entry2_spacing.get()-1)
                    entry3_spacing.set(entry3_spacing.get()-1)
                    entry4_spacing.set(entry4_spacing.get()-1)
                    entry5_spacing.set(entry5_spacing.get()-1)
                    save_location_missing_spacing.set(save_location_missing_spacing.get()-1)
                if int(Number_Of_Particles_To_Track.get()) > 1:
                    Particle_Focus_Menu_Function()
                    
                Auto_Contrast_Button_Canvas = canvas1.create_window(200,open_window_spacing.get()*gap,window=Auto_Contrast_Button)
                #Contrast_Adjust_Button_Canvas = canvas1.create_window(300,open_window_spacing.get()*gap,window=Contrast_Adjust_Button)
                Contrast_Adjust_Checkbox_Button_Canvas = canvas1.create_window(350,open_window_spacing.get()*gap,window=Contrast_Adjust_Checkbox_Button)
                
                missing_entries_label_canvas = canvas1.create_window(100,save_location_missing_spacing.get()*gap,window=missing_entries_label)
                Missing_Entries_Entry_Canvas = canvas1.create_window(170,save_location_missing_spacing.get()*gap,window=Missing_Entries_Entry)
                x_coordinate_label_canvas = canvas1.create_window(60,x_input_spacing.get()*gap,window=x_coordinate_label)
                X_Coordinate_Entry_entry_canvas = canvas1.create_window(225,x_input_spacing.get()*gap,window=X_Coordinate_Entry)
                y_coordinate_label_Canvas = canvas1.create_window(60,y_input_spacing.get()*gap,window=y_coordinate_label)
                Y_Coordinate_Entry_canvas = canvas1.create_window(225,y_input_spacing.get()*gap,window=Y_Coordinate_Entry)
                append_next_Button_Canvas = canvas1.create_window(120,set_val_spacing.get()*gap,window=append_next_Button)
                Save_Output_Button_Canvas = canvas1.create_window(250,save_location_missing_spacing.get()*gap,window=Save_Output_Button)
                
                t1_label_canvas = canvas1.create_window(50,entry1_spacing.get()*gap,window=t1_label)
                t1_entry_canvas = canvas1.create_window(75,entry1_spacing.get()*gap,window=t1_entry)
                x1_label_canvas = canvas1.create_window(95,entry1_spacing.get()*gap,window=x1_label)
                x1_entry_canvas = canvas1.create_window(125,entry1_spacing.get()*gap,window=x1_entry)
                y1_label_canvas = canvas1.create_window(155,entry1_spacing.get()*gap,window=y1_label)
                y1_entry_canvas = canvas1.create_window(185,entry1_spacing.get()*gap,window=y1_entry)
                z1_label_canvas = canvas1.create_window(215,entry1_spacing.get()*gap,window=z1_label)
                z1_entry_canvas = canvas1.create_window(245,entry1_spacing.get()*gap,window=z1_entry)
                t1checked_label_canvas = canvas1.create_window(295,entry1_spacing.get()*gap,window=t1checked_label)
                t1checked_entry_canvas = canvas1.create_window(345,entry1_spacing.get()*gap,window=t1checked_entry)
                t_1.set(1)
                
                if Times_On_Pages_To_Display.get() > 1:
                    t2_label_canvas = canvas1.create_window(50,entry2_spacing.get()*gap,window=t2_label)
                    t2_entry_canvas = canvas1.create_window(75,entry2_spacing.get()*gap,window=t2_entry)
                    x2_label_canvas = canvas1.create_window(95,entry2_spacing.get()*gap,window=x2_label)
                    x2_entry_canvas = canvas1.create_window(125,entry2_spacing.get()*gap,window=x2_entry)
                    y2_label_canvas = canvas1.create_window(155,entry2_spacing.get()*gap,window=y2_label)
                    y2_entry_canvas = canvas1.create_window(185,entry2_spacing.get()*gap,window=y2_entry)
                    z2_label_canvas = canvas1.create_window(215,entry2_spacing.get()*gap,window=z2_label)
                    z2_entry_canvas = canvas1.create_window(245,entry2_spacing.get()*gap,window=z2_entry)
                    t2checked_label_canvas = canvas1.create_window(295,entry2_spacing.get()*gap,window=t2checked_label)
                    t2checked_entry_canvas = canvas1.create_window(345,entry2_spacing.get()*gap,window=t2checked_entry)
                    t_2.set(2)
                if Times_On_Pages_To_Display.get()>2:
                    t3_label_canvas = canvas1.create_window(50,entry3_spacing.get()*gap,window=t3_label)
                    t3_entry_canvas = canvas1.create_window(75,entry3_spacing.get()*gap,window=t3_entry)
                    x3_label_canvas = canvas1.create_window(95,entry3_spacing.get()*gap,window=x3_label)
                    x3_entry_canvas = canvas1.create_window(125,entry3_spacing.get()*gap,window=x3_entry)
                    y3_label_canvas = canvas1.create_window(155,entry3_spacing.get()*gap,window=y3_label)
                    y3_entry_canvas = canvas1.create_window(185,entry3_spacing.get()*gap,window=y3_entry)
                    z3_label_canvas = canvas1.create_window(215,entry3_spacing.get()*gap,window=z3_label)
                    z3_entry_canvas = canvas1.create_window(245,entry3_spacing.get()*gap,window=z3_entry)
                    t3checked_label_canvas = canvas1.create_window(295,entry3_spacing.get()*gap,window=t3checked_label)
                    t3checked_entry_canvas = canvas1.create_window(345,entry3_spacing.get()*gap,window=t3checked_entry)
                    t_3.set(3)
                if Times_On_Pages_To_Display.get() >3:
                    t4_label_canvas = canvas1.create_window(50,entry4_spacing.get()*gap,window=t4_label)
                    t4_entry_canvas = canvas1.create_window(75,entry4_spacing.get()*gap,window=t4_entry)
                    x4_label_canvas = canvas1.create_window(95,entry4_spacing.get()*gap,window=x4_label)
                    x4_entry_canvas = canvas1.create_window(125,entry4_spacing.get()*gap,window=x4_entry)
                    y4_label_canvas = canvas1.create_window(155,entry4_spacing.get()*gap,window=y4_label)
                    y4_entry_canvas = canvas1.create_window(185,entry4_spacing.get()*gap,window=y4_entry)
                    z4_label_canvas = canvas1.create_window(215,entry4_spacing.get()*gap,window=z4_label)
                    z4_entry_canvas = canvas1.create_window(245,entry4_spacing.get()*gap,window=z4_entry)
                    t4checked_label_canvas = canvas1.create_window(295,entry4_spacing.get()*gap,window=t4checked_label)
                    t4checked_entry_canvas = canvas1.create_window(345,entry4_spacing.get()*gap,window=t4checked_entry)
                    t_4.set(4)
                if Times_On_Pages_To_Display.get() >4:
                    t5_label_canvas = canvas1.create_window(50,entry5_spacing.get()*gap,window=t5_label)
                    t5_entry_canvas = canvas1.create_window(75,entry5_spacing.get()*gap,window=t5_entry)
                    x5_label_canvas = canvas1.create_window(95,entry5_spacing.get()*gap,window=x5_label)
                    x5_entry_canvas = canvas1.create_window(125,entry5_spacing.get()*gap,window=x5_entry)
                    y5_label_canvas = canvas1.create_window(155,entry5_spacing.get()*gap,window=y5_label)
                    y5_entry_canvas = canvas1.create_window(185,entry5_spacing.get()*gap,window=y5_entry)
                    z5_label_canvas = canvas1.create_window(215,entry5_spacing.get()*gap,window=z5_label)
                    z5_entry_canvas = canvas1.create_window(245,entry5_spacing.get()*gap,window=z5_entry)
                    t5checked_label_canvas = canvas1.create_window(295,entry5_spacing.get()*gap,window=t5checked_label)
                    t5checked_entry_canvas = canvas1.create_window(345,entry5_spacing.get()*gap,window=t5checked_entry)
                    t_5.set(5)
        if Organized_Files_Done.get() == 1:
            global time_displayed
            time_displayed = 0
            global Entry_Tracked
            Entry_Tracked = 0
            global Folder_Z_Values
            if Derivative_Check_Variable.get() == 0:
                Folder_Z_Values = np.zeros(Ascending_Order.shape[0])
                for x in range(Ascending_Order.shape[0]):
                    Folder_Z_Values[x] = float(Ascending_Order[x][0].name)
            if Derivative_Check_Variable.get() == 1:
                Folder_Z_Values = np.arange(Z_Resolution_Variable.get()*Derivative_Image_Array.shape[1],Z_Starting_Point.get()-Z_Resolution_Variable.get(),-Z_Resolution_Variable.get())
            
            matplotlib.rcParams['toolbar'] = 'None'
            global ax
            fig, ax = plt.subplots(1,1,figsize=(5,5),dpi=160,tight_layout=True)
            
            global X
            if Derivative_Check_Variable.get() == 0:
                X = np.moveaxis(Phase_T[:,:,:,:],[1,2,3],[3,1,2])
            if Derivative_Check_Variable.get() == 1:
                X = np.moveaxis(Derivative_Image_Array[:,:,:,:],[1,2,3],[3,1,2])
            global tracker
            tracker = IndexTracker(ax,X,Folder_Z_Values,time_displayed,Entry_Tracked)
            fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
            fig.canvas.mpl_connect('button_press_event', tracker.onclick)
            fig.canvas.mpl_connect('key_press_event',tracker.time_swap)
            fig.canvas.mpl_connect('key_release_event', tracker.on_key_release)
            thismanager = plt.get_current_fig_manager()
            plt.show()

    def Append_List():
        Z_Location.set(str(Z_Slice_Present))
        #z_selection_var.set(Z_Slice_Present)
        Particle_Locations[Particle_of_Focus.get(),time_seen,1] = X_Coordinate.get()
        Particle_Locations[Particle_of_Focus.get(),time_seen,2] = Y_Coordinate.get()
        Particle_Locations[Particle_of_Focus.get(),time_seen,3] = Z_Slice_Present
        Particle_Locations[Particle_of_Focus.get(),time_seen,4] = 1
        Missing_Entries.set(int(np.count_nonzero(Particle_Locations[:,:,4]==0)))
        
        print('First time',First_Time_Entry_Displayed.get())
        print('time seen',time_seen+1)
        print('last time',First_Time_Entry_Displayed.get()+4)
        print('entry tracked',Entry_Tracked)
        if First_Time_Entry_Displayed.get() <= time_seen+1 <= First_Time_Entry_Displayed.get()+4:
            if Entry_Tracked == 0:
                x_1.set(X_Coordinate.get())
                y_1.set(Y_Coordinate.get())
                z_1.set(Z_Slice_Present)
                t1_checked.set('Yes')
            if Entry_Tracked == 1:
                x_2.set(X_Coordinate.get())
                y_2.set(Y_Coordinate.get())
                z_2.set(Z_Slice_Present)
                t2_checked.set('Yes')
            if Entry_Tracked == 2:
                x_3.set(X_Coordinate.get())
                y_3.set(Y_Coordinate.get())
                z_3.set(Z_Slice_Present)
                t3_checked.set('Yes')
            if Entry_Tracked == 3:
                x_4.set(X_Coordinate.get())
                y_4.set(Y_Coordinate.get())
                z_4.set(Z_Slice_Present)
                t4_checked.set('Yes')
            if Entry_Tracked == 4:
                x_5.set(X_Coordinate.get())
                y_5.set(Y_Coordinate.get())
                z_5.set(Z_Slice_Present)
                t5_checked.set('Yes')
        
    def Input_Directory():
        if Derivative_Check_Variable.get() == 0:
            Input_Directory_Text.set('')
            Input_Direction_Chosen = filedialog.askdirectory(parent=root,title='Choose a directory')
            Input_Directory_Entry.insert(END,Input_Direction_Chosen)
        if Derivative_Check_Variable.get() == 1:
            Derivative_Input_File_Name_Open = filedialog.askopenfilename()
            Derivative_Input_File_Name.set(Derivative_Input_File_Name_Open)
            if Derivative_Input_File_Name.get() == '':
                Derivative_Input_File_Name.set('(Required)')

    def Move_Left():
        moved = 0
        if moved == 0:
            if First_Time_Entry_Displayed.get() == 1:
                First_Time_Entry_Displayed.set(int(Times_of_Interest.get()) - (int(Times_of_Interest.get()) % 5) + 1)
                moved = 1
        if moved == 0:
            if First_Time_Entry_Displayed.get() != 1:
                First_Time_Entry_Displayed.set(First_Time_Entry_Displayed.get()-5)
        Move_Page()

    def Move_Right():
        moved = 0
        if moved == 0:
            if First_Time_Entry_Displayed.get() == int(Times_of_Interest.get()) - (int(Times_of_Interest.get()) % 5) + 1:
                First_Time_Entry_Displayed.set(1)
                moved = 1
        if moved == 0:
            if First_Time_Entry_Displayed.get() != int(Times_of_Interest.get()) - (int(Times_of_Interest.get()) % 5) + 1:
                First_Time_Entry_Displayed.set(First_Time_Entry_Displayed.get()+5)
        Move_Page()

    def End_Time_Changed(*args):
        if Launched_Window.get() == 0:
            try:
                int(Times_of_Interest.get())
            except ValueError:
                pass
            else:
                Missing_Entries.set(int(Times_of_Interest.get()))

    def Jump_To_Entry(*args):
        try:
            int(jump_to_value.get())
        except ValueError:
            pass
        else:
            if int(jump_to_value.get())%5 == 0:
                First_Time_Entry_Displayed.set(int(jump_to_value.get())-4)
            if int(jump_to_value.get())%5 != 0:
                First_Time_Entry_Displayed.set(int(jump_to_value.get())-(int(jump_to_value.get())%5)+1)
            Move_Page()

    def Finished_Check():
        if np.count_nonzero(Particle_Locations[:,:,4]==0)!=0:
            popup = Tk()
            canvas2 = Canvas(popup, relief = 'raised')
            canvas2.pack(fill=BOTH, expand=YES)
            popup.title("Tkinter window")
            
            def Close_And_Finish():
                popup.destroy()
                Finished()
                pass
            def Close():
                popup.destroy()
                pass
            
            Warning_Label = Label(popup,text='Not all entries are filled, do you wish to continue?')
            Yes_Button = Button(popup,text='Yes',command=Close_And_Finish,width=10)
            No_Button = Button(popup,text='No',command=Close,width=10)
            
            Warning_Label_Canvas = canvas2.create_window(150,20,window=Warning_Label)
            Yes_Button_Canvas = canvas2.create_window(95,48,window=Yes_Button)
            No_Button_Canvas = canvas2.create_window(195,48,window=No_Button)
            
            w = 300 # width for the Tk root
            h = 75 # height for the Tk root
            ws = popup.winfo_screenwidth() # width of the screen
            hs = popup.winfo_screenheight() # height of the screen
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
            popup.mainloop()
            
        if np.count_nonzero(Particle_Locations[:,:,4]==0)==0:
            Finished()

    def Change_Focus(*args):
        try:
            int(Particle_of_Focus_String.get())
        except ValueError:
            pass
        else:
            Particle_of_Focus.set(int(Particle_of_Focus_String.get())-1)
            Move_Page()
            
    def Time_Stamp_Text_File():
        TimeStamp_Text_File_Name_Open = filedialog.askopenfilename()
        TimeStamp_Text_File_Name.set(TimeStamp_Text_File_Name_Open)
        TimeStamp_Text_File_Name_Shortened.set(TimeStamp_Text_File_Name_Open.split('/')[-1])
        Enter_Time_Stamp_Data()
        
    def Enter_Time_Stamp_Data():
        textfile = open(TimeStamp_Text_File_Name.get(),'r')
        
        for textfile_length,entry in enumerate(textfile):
            pass
            
        textfile_length += 1
        Time_Stamp_Array = np.zeros((textfile_length))
        textfile = open(TimeStamp_Text_File_Name.get(),'r')
        for line,entry in enumerate(textfile):
            Time_Stamp_Array[line] = entry.split(' ')[-2]
        
        global Time_Stamp_Array_Times_of_Interest
        Time_Stamp_Array_Times_of_Interest = Time_Stamp_Array[Initial_Time_Point_Speeds.get()-1:Initial_Time_Point_Speeds.get()+int(Times_of_Interest.get())-1]
    
    def Z_Input_Display(*args):
        Z_Resolution_Label_Canvas = canvas1.create_window(425,particle_number_spacing.get()*gap,window=Z_Resolution_Label)
        Z_Resolution_Entry_Canvas = canvas1.create_window(485,particle_number_spacing.get()*gap,window=Z_Resolution_Entry)
        Z_Starting_Point_Label_Canvas = canvas1.create_window(575,particle_number_spacing.get()*gap,window=Z_Starting_Point_Label)
        Z_Starting_Point_Entry_Canvas = canvas1.create_window(655,particle_number_spacing.get()*gap,window=Z_Starting_Point_Entry)
        
        Input_Directory_Button_Canvas = canvas1.create_window(75,input_dir_spacing.get()*gap,window=Input_Directory_Button)
        Input_Directory_Entry_Canvas = canvas1.create_window(431,input_dir_spacing.get()*gap,window=Input_Directory_Entry)
        canvas1.delete(Input_Directory_Button_Canvas)
        canvas1.delete(Input_Directory_Entry_Canvas)
        Input_Derivative_File_Button_Canvas = canvas1.create_window(75,input_dir_spacing.get()*gap,window=Input_Derivative_File_Button)
        Derivative_File_Entry_Canvas = canvas1.create_window(431,input_dir_spacing.get()*gap,window=Derivative_File_Entry)
        canvas1.delete(Input_Derivative_File_Button_Canvas)
        canvas1.delete(Derivative_File_Entry_Canvas)
        
        if Derivative_Check_Variable.get() == 0:
            canvas1.delete(Z_Resolution_Label_Canvas)
            canvas1.delete(Z_Resolution_Entry_Canvas)
            canvas1.delete(Z_Starting_Point_Label_Canvas)
            canvas1.delete(Z_Starting_Point_Entry_Canvas)
            Input_Directory_Button_Canvas = canvas1.create_window(75,input_dir_spacing.get()*gap,window=Input_Directory_Button)
            Input_Directory_Entry_Canvas = canvas1.create_window(431,input_dir_spacing.get()*gap,window=Input_Directory_Entry)
        if Derivative_Check_Variable.get() == 1:
            Input_Derivative_File_Button_Canvas = canvas1.create_window(75,input_dir_spacing.get()*gap,window=Input_Derivative_File_Button)
            Derivative_File_Entry_Canvas = canvas1.create_window(431,input_dir_spacing.get()*gap,window=Derivative_File_Entry)

    def Stall(*args):
        if Initiated_Contrast_Check.get() == 1:
            contrast_updater.update_contrast()
    
    def Applying_Update(*args):
        Apply_Update_Notice_Label_Canvas = canvas1.create_window(625,open_window_spacing.get()*28,window=Apply_Update_Notice_Label)
        root.update()
        
    def Adjust_Contrast_From_Popup(*args):
        if Contrast_Button_Checkbox_value.get() == 1:
            Contrast_Button_Check.set(1)
            Applying_Update()
            tracker.update()
            
    def Adjust_Contrast_From_Checkbox(*args):
        if Contrast_Button_Checkbox_value.get() == 1:
            Contrast_Button_Checkbox_value_Prior.set(0)
        if Contrast_Button_Checkbox_value.get() == 0:
            Contrast_Button_Checkbox_value_Prior.set(1)
        if Contrast_Button_Check.get() == 1 or Auto_Contrast_Pressed.get() == 1:
            Applying_Update()
            tracker.update()

    def Contrast_Popup(*args):
        Opening_Contrast_Window_Label_Canvas = canvas1.create_window(645,open_window_spacing.get()*28,window=Opening_Contrast_Window_Label)
        root.update()
        
        win = Tk()
        Image_Frame = Frame(win,height=400,width=800,bg='gray')
        
        Distribution = np.unique(np.round(X[time_seen,:,:,:],4),return_counts=True)

        hologram_mean = np.mean(X[time_seen,:,:,:])
        hologram_std = np.std(X[time_seen,:,:,:])
        hologram_min = np.min(X[time_seen,:,:,:])
        hologram_max = np.max(X[time_seen,:,:,:])
        
        Distribution_min = np.min(Distribution[1])
        Distribution_max = np.max(Distribution[1])

        fig,ax = plt.subplots()
        plt.plot(Distribution[0],Distribution[1],color='black')
        plt.tight_layout()
        plt.axis('on')

        Image_Frame.pack()


        Slider_Frame = Frame(win,height=150,width=500)
        Slider_Canvas = Canvas(master=Slider_Frame,bg='gray')
        Slider_Canvas.pack(side=TOP,fill=BOTH,expand=True)

        Lower_Contrast_Value.set(hologram_mean-2*hologram_std)
        Upper_Contrast_Value.set(hologram_mean+2*hologram_std)

        print(f'Lower: {Lower_Contrast_Value.get()}, Upper: {Upper_Contrast_Value.get()}')

        middle_position = 340
        gap = 28
        Lower_Slider_Positon = gap
        Upper_Slider_Position = (Lower_Slider_Positon/gap + 2) * gap - 8
        Start_Button_Position = (Upper_Slider_Position/gap + 1) * gap +10

        Lower_Contrast_Slider = Scale(Slider_Frame,from_=hologram_min,to=hologram_max,orient=HORIZONTAL,variable=Lower_Contrast_Value,resolution=0.1)
        Lower_Contrast_Slider_Canvas = Slider_Canvas.create_window(middle_position,Lower_Slider_Positon,window=Lower_Contrast_Slider)

        Upper_Contrast_Slider = Scale(Slider_Frame,from_=hologram_min,to=hologram_max,orient=HORIZONTAL,variable=Upper_Contrast_Value,resolution=0.1)
        Upper_Contrast_Slider_Canvas = Slider_Canvas.create_window(middle_position,Upper_Slider_Position,window=Upper_Contrast_Slider)

        Adjust_Contrast_Button = Button(Slider_Frame,text='Display new contrast line',command=Adjust_Contrast_From_Popup)
        Adjust_Contrast_Button_Canvas = Slider_Canvas.create_window(middle_position+5,Start_Button_Position,window=Adjust_Contrast_Button)
        
        global contrast_updater
        contrast_updater = Contrast_Drawing(fig,ax,hologram_min,hologram_max,Distribution_min,Distribution_max,hologram_mean,hologram_std)
        print('Contrast updater run')
        #Lower_Contrast_Value.trace('w',contrast_updater.update_contrast)
        #Upper_Contrast_Value.trace('w',contrast_updater.update_contrast)

        Image_Canvas = FigureCanvasTkAgg(fig, master=Image_Frame)
        Image_Canvas.draw()
        Image_Canvas.get_tk_widget().pack(side=TOP,fill=BOTH, expand=YES)
        Slider_Frame.pack(side=TOP,fill=BOTH,expand=True)

        Initiated_Contrast_Check.set(1)
        canvas1.delete(Opening_Contrast_Window_Label_Canvas)
        
        win.lift()

        w = middle_position*2 # width for the Tk root
        h = 620 # height for the Tk root
        ws = win.winfo_screenwidth() # width of the screen
        hs = win.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.mainloop()
    
    def Auto_Contrast(*args):
        hologram_mean = np.mean(X[time_seen,:,:,:])
        hologram_std = np.std(X[time_seen,:,:,:])
        
        Lower_Contrast_Value.set(hologram_mean-2*hologram_std)
        Upper_Contrast_Value.set(hologram_mean+2*hologram_std)
        
        Auto_Contrast_Pressed.set(1)
        print(Contrast_Button_Checkbox_value.get())
        
        Applying_Update()
        
        tracker.update()

        
    Variable_Minimize = 0
    if Variable_Minimize == 0:
        '''
            All variables used in the program are designated here as Integer or String variables (IntVar and StringVar respectively).
        '''
        X_Coordinate = IntVar()
        Y_Coordinate = IntVar()
        Times_of_Interest = StringVar()
        Times_of_Interest.set('1')
        Times_of_Interest.trace('w',End_Time_Changed)
        Input_Directory_Text = StringVar()
        Input_Directory_Text.set('(Required)')
        #Input_Directory_Text.set('F:/CURRENT_TEST_SET_(12.04.20)_2019.05.01_15-21/Niko_Test/Manual_Tracking/Holograms/Phase')
        Organized_Files_Done = IntVar()
        Z_Location = IntVar()
        x_1,x_2,x_3,x_4,x_5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        y_1,y_2,y_3,y_4,y_5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        z_1,z_2,z_3,z_4,z_5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        t_1,t_2,t_3,t_4,t_5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        t1_checked,t2_checked,t3_checked,t4_checked,t5_checked = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        t1_checked.set('No')
        t2_checked.set('No')
        t3_checked.set('No')
        t4_checked.set('No')
        t5_checked.set('No')
        First_Time_Entry_Displayed = IntVar()
        First_Time_Entry_Displayed.set(1)
        Times_On_Pages_To_Display = IntVar()
        Missing_Entries = IntVar()
        Missing_Entries.set(int(Times_of_Interest.get()))
        starttimes_spacing,timestamp_spacing,input_dir_spacing,derivative_check_spacing,particle_number_spacing,open_window_spacing,x_input_spacing,y_input_spacing,set_val_spacing,arrows_jumping_spacing,entry1_spacing,entry2_spacing,entry3_spacing,entry4_spacing,entry5_spacing,save_location_missing_spacing = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        starttimes_spacing.set(1)
        timestamp_spacing.set(starttimes_spacing.get()+1)
        input_dir_spacing.set(timestamp_spacing.get()+1)
        derivative_check_spacing.set(input_dir_spacing.get()+1)
        particle_number_spacing.set(derivative_check_spacing.get()+1)
        open_window_spacing.set(particle_number_spacing.get()+1)
        x_input_spacing.set(open_window_spacing.get()+1)
        y_input_spacing.set(x_input_spacing.get()+1)
        set_val_spacing.set(y_input_spacing.get()+1)
        arrows_jumping_spacing.set(set_val_spacing.get()+1)
        entry1_spacing.set(arrows_jumping_spacing.get()+1)
        entry2_spacing.set(entry1_spacing.get()+1)
        entry3_spacing.set(entry2_spacing.get()+1)
        entry4_spacing.set(entry3_spacing.get()+1)
        entry5_spacing.set(entry4_spacing.get()+1)
        save_location_missing_spacing.set(entry5_spacing.get()+1)
        Launched_Window = IntVar()
        jump_to_value = StringVar()
        jump_to_value.set('0')
        jump_to_value.trace('w',Jump_To_Entry)
        Number_Of_Particles_To_Track = StringVar()
        Number_Of_Particles_To_Track.set('1')
        Number_Of_Particles_To_Track.trace('w',Adjust_Particles_Tracked_Size_Check)
        Particle_of_Focus_String = StringVar()
        Particle_of_Focus_String.set('1')
        Particle_of_Focus_String.trace('w',Change_Focus)
        Particle_of_Focus = IntVar()
        Particle_of_Focus.set(0)
        Initial_Time_Point_Speeds = IntVar()
        Initial_Time_Point_Speeds.set(1)
        TimeStamp_Text_File_Name = StringVar()
        #TimeStamp_Text_File_Name.set('F:/CURRENT_TEST_SET_(12.04.20)_2019.05.01_15-21/timestamps.txt')
        TimeStamp_Text_File_Name_Shortened = StringVar()
        TimeStamp_Text_File_Name_Shortened.set('(Required)')
        XY_Resolution_Variable = DoubleVar()
        XY_Resolution_Variable.set(0.1285)
        Z_Resolution_Variable = DoubleVar()
        Z_Resolution_Variable.set(2)
        Z_Starting_Point = DoubleVar()
        Z_Starting_Point.set(int(0))
        Derivative_Check_Variable = IntVar()
        Derivative_Check_Variable.trace('w',Z_Input_Display)
        Derivative_Input_File_Name = StringVar()
        #Derivative_Input_File_Name.set('F:/CURRENT_TEST_SET_(12.04.20)_2019.05.01_15-21/Niko_Test/Phase_Deriv/Testing/1_3_Deriv_0_0_1.tif')
        Derivative_Input_File_Name.set('(Required)')
        Window_Opened_Check = IntVar()
        #Enter_Time_Stamp_Data()
        Lower_Bound_Contrast_Limit = DoubleVar()
        Lower_Bound_Contrast_Value = DoubleVar()
        Upper_Bound_Contrast_Limit = DoubleVar()
        Upper_Bound_Contrast_Value = DoubleVar()
        holo_min = DoubleVar()
        holo_max = DoubleVar()
        holo_contrast_min,holo_contrast_max = IntVar(),IntVar()
        holo_mean,holo_std = DoubleVar(),DoubleVar()
        Lower_Contrast_Last_Value = IntVar()
        Upper_Contrast_Last_Value = IntVar()
        Contrast_Button_Check = IntVar()
        Contrast_Button_Checkbox_value = IntVar()
        Contrast_Button_Checkbox_value.trace('w',Adjust_Contrast_From_Checkbox)
        Contrast_Button_Checkbox_value_Prior = IntVar()
        Lower_Contrast_Value = DoubleVar()
        Upper_Contrast_Value = DoubleVar()
        Lower_Contrast_Value.trace('w',Stall)
        Upper_Contrast_Value.trace('w',Stall)
        Auto_Contrast_Pressed = IntVar()
        Initiated_Contrast_Check = IntVar()
        
    Label_Minimize = 0
    if Label_Minimize == 0:
        '''
            Labels are designated in this section, they are the text that is written on the GUI.
        '''
        x_coordinate_label = Label(root,text='X Input')
        y_coordinate_label = Label(root,text='Y Input')
        Times_of_Interest_Label = Label(root,text='Number of Time Points')
        missing_entries_label = Label(root,text='Unentered Entries:')
        t1_label,t2_label,t3_label,t4_label,t5_label = Label(root,text='T:'),Label(root,text='T:'),Label(root,text='T:'),Label(root,text='T:'),Label(root,text='T:')
        x1_label,x2_label,x3_label,x4_label,x5_label = Label(root,text='X:'),Label(root,text='X:'),Label(root,text='X:'),Label(root,text='X:'),Label(root,text='X:')
        y1_label,y2_label,y3_label,y4_label,y5_label = Label(root,text='Y:'),Label(root,text='Y:'),Label(root,text='Y:'),Label(root,text='Y:'),Label(root,text='Y:')
        z1_label,z2_label,z3_label,z4_label,z5_label = Label(root,text='Z:'),Label(root,text='Z:'),Label(root,text='Z:'),Label(root,text='Z:'),Label(root,text='Z:')
        t1checked_label,t2checked_label,t3checked_label,t4checked_label,t5checked_label = Label(root,text='Entered:'),Label(root,text='Entered:'),Label(root,text='Entered:'),Label(root,text='Entered:'),Label(root,text='Entered:')
        jump_to_label = Label(root,text='Jump to:')
        Number_Of_Particles_To_Track_Label = Label(root,text='Number of Particles to Track:')
        Particle_Of_Focus_Label = Label(root,text='Particle of Focus')
        Initial_Time_Point_Speeds_Label = Label(root,text='Initial Time Point In Data:')
        XY_Resolution_Label = Label(root,text='X/Y Resolution:')
        Z_Resolution_Label = Label(root,text='Z Resolution:')
        Z_Starting_Point_Label = Label(root,text='Lowest Z-slice Value:')
        Apply_Update_Notice_Label = Label(root,text='Applying Update, Please Wait...')
        #Apply_Update_Finished_Label = Label(root,text='Finished Updating')
        Opening_Contrast_Window_Label = Label(root,text='Opening Contrast Popup, Please Wait')
    
    Entry_Minimize = 0
    if Entry_Minimize == 0:
        '''
            All entries are designated here, entries are the spaces for values to be displayed or modified.  Some can only be changed prior to opening the window to display the reconstructions.
            Only before:
                Number of Time Points
                Number of Particles to Track
            Any time:
                Initial Time Point in Data
                X Coordinate
                Y Coordinate
                Particle Location Data (t#,x#,y#,z#,t#_checked)
        '''
        X_Coordinate_Entry = Entry(root,textvariable=X_Coordinate)
        Y_Coordinate_Entry = Entry(root,textvariable=Y_Coordinate)
        Times_of_Interest_Entry = Entry(root,textvariable=Times_of_Interest,width=5)
        Input_Directory_Entry = Entry(root,textvariable=Input_Directory_Text,width=87)
        Derivative_File_Entry = Entry(root,textvariable=Derivative_Input_File_Name,width=87)
        Missing_Entries_Entry = Entry(root,textvariable=Missing_Entries,width=5)
        jump_to_entry = Entry(root,textvariable=jump_to_value,width=5)
        Number_Of_Particles_To_Track_Entry = Entry(root,textvariable=Number_Of_Particles_To_Track,width=5)
        entry_widtht = 3
        entry_widthx = 6
        entry_widthy = 6
        entry_widthz = 6
        entry_widthtc = 6
        t1_entry,t2_entry,t3_entry,t4_entry,t5_entry = Entry(root,textvariable=t_1,width=entry_widtht),Entry(root,textvariable=t_2,width=entry_widtht),Entry(root,textvariable=t_3,width=entry_widtht),Entry(root,textvariable=t_4,width=entry_widtht),Entry(root,textvariable=t_5,width=entry_widtht)
        x1_entry,x2_entry,x3_entry,x4_entry,x5_entry = Entry(root,textvariable=x_1,width=entry_widthx),Entry(root,textvariable=x_2,width=entry_widthx),Entry(root,textvariable=x_3,width=entry_widthx),Entry(root,textvariable=x_4,width=entry_widthx),Entry(root,textvariable=x_5,width=entry_widthx)
        y1_entry,y2_entry,y3_entry,y4_entry,y5_entry = Entry(root,textvariable=y_1,width=entry_widthy),Entry(root,textvariable=y_2,width=entry_widthy),Entry(root,textvariable=y_3,width=entry_widthy),Entry(root,textvariable=y_4,width=entry_widthy),Entry(root,textvariable=y_5,width=entry_widthy)
        z1_entry,z2_entry,z3_entry,z4_entry,z5_entry = Entry(root,textvariable=z_1,width=entry_widthz),Entry(root,textvariable=z_2,width=entry_widthz),Entry(root,textvariable=z_3,width=entry_widthz),Entry(root,textvariable=z_4,width=entry_widthz),Entry(root,textvariable=z_5,width=entry_widthz)
        t1checked_entry,t2checked_entry,t3checked_entry,t4checked_entry,t5checked_entry = Entry(root,textvariable=t1_checked,width=entry_widthtc),Entry(root,textvariable=t2_checked,width=entry_widthtc),Entry(root,textvariable=t3_checked,width=entry_widthtc),Entry(root,textvariable=t4_checked,width=entry_widthtc),Entry(root,textvariable=t5_checked,width=entry_widthtc)
        Initial_Time_Point_Speeds_Entry = Entry(root,textvariable=Initial_Time_Point_Speeds,width=5)
        TimeStamp_Text_File_Entry = Entry(root,textvariable=TimeStamp_Text_File_Name_Shortened,width=20)
        XY_Resolution_Entry = Entry(root,textvariable=XY_Resolution_Variable,width=7)
        Z_Resolution_Entry = Entry(root,textvariable=Z_Resolution_Variable,width=5)
        Z_Starting_Point_Entry = Entry(root,textvariable=Z_Starting_Point,width=5)
    
    Button_Minimize = 0
    if Button_Minimize == 0:
        Open_Window_Button = Button(root,text='Open Image Window',command=Launch_Window,width=18)
        Input_Directory_Button = Button(root,text='Input Directory',command=Input_Directory,width=18)
        Input_Derivative_File_Button = Button(root,text='Input Derivative Directory',command=Input_Directory,width=18)
        append_next_Button = Button(root,text='Edit Current Time Value',command=Append_List)
        Left_Arrow_Button = Button(root,text='<--',command=Move_Left)
        Right_Arrow_Button = Button(root,text='-->',command=Move_Right)
        Save_Output_Button = Button(root,text='Save Locations',command=Finished_Check)
        TimeStamp_Text_File_Button = Button(root,text='Input Timestamp File',command=Time_Stamp_Text_File,width=18)
        Derivative_Check_Button = Checkbutton(root,text="Check if using derivative of reconstructions (from Niko's Derivative Function only)", variable=Derivative_Check_Variable)
        Contrast_Adjust_Button = Button(root,text='Contrast',command=Contrast_Popup)
        Contrast_Adjust_Checkbox_Button = Checkbutton(root,text="Apply Contrast Adjustment",variable=Contrast_Button_Checkbox_value)
        Auto_Contrast_Button = Button(root,text='Auto Contrast',command=Auto_Contrast)
        
    
    Canvas_Minimize = 0
    if Canvas_Minimize == 0:
        gap = 28
       
        Times_of_Interest_Label_Canvas = canvas1.create_window(75,starttimes_spacing.get()*gap,window=Times_of_Interest_Label)
        Times_of_Interest_Entry_Canvas = canvas1.create_window(185,starttimes_spacing.get()*gap,window=Times_of_Interest_Entry)
        Initial_Time_Point_Speeds_Label_Canvas = canvas1.create_window(425,timestamp_spacing.get()*gap,window=Initial_Time_Point_Speeds_Label)
        Initial_Time_Point_Speeds_Entry_Canvas = canvas1.create_window(520,timestamp_spacing.get()*gap,window=Initial_Time_Point_Speeds_Entry)
        TimeStamp_Text_File_Button_Canvas = canvas1.create_window(75,timestamp_spacing.get()*gap,window=TimeStamp_Text_File_Button)
        TimeStamp_Text_File_Entry_Canvas = canvas1.create_window(230,timestamp_spacing.get()*gap,window=TimeStamp_Text_File_Entry)
        Input_Directory_Button_Canvas = canvas1.create_window(75,input_dir_spacing.get()*gap,window=Input_Directory_Button)
        Input_Directory_Entry_Canvas = canvas1.create_window(431,input_dir_spacing.get()*gap,window=Input_Directory_Entry)
        Derivative_Check_Button_Canvas = canvas1.create_window(300,derivative_check_spacing.get()*gap,window=Derivative_Check_Button)
        Number_Of_Particles_To_Track_Label_Canvas = canvas1.create_window(85,particle_number_spacing.get()*gap,window=Number_Of_Particles_To_Track_Label)
        Number_Of_Particles_To_Track_Entry_Canvas = canvas1.create_window(185,particle_number_spacing.get()*gap,window=Number_Of_Particles_To_Track_Entry)
        XY_Resolution_Label_Canvas = canvas1.create_window(280,particle_number_spacing.get()*gap,window=XY_Resolution_Label)
        XY_Resolution_Entry_Canvas = canvas1.create_window(350,particle_number_spacing.get()*gap,window=XY_Resolution_Entry)
        Open_Window_Button_Canvas = canvas1.create_window(75,open_window_spacing.get()*gap,window=Open_Window_Button)
    
    root.title("Tkinter window")
    w = 750 # width for the Tk root
    h = (save_location_missing_spacing.get()+1)*gap # height for the Tk root
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws/5) - (w/2)
    y = (hs/3) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()