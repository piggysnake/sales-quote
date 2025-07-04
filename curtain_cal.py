import tkinter as tk
from tkinter import scrolledtext
import math
import re

class TranslatorFunc:
    def __init__(self, text):
        self.text = text
        self.replacements = {
            "布": "curtain",
            "纱": "sheer",
            "卷帘": "roller blind",
            "帘高": " fabric height,",
            "一个":" one ",
            "两个":" two ",
            "顶装": "ceiling mount,",
            "侧装": "wall mount,",
            "宽": "w",
            "实际高": "h",
            "高": "h",
            "主卧": "Master bedroom",
            "左": "left ",
            "右": "right ",
            "卧室": "bedroom",
            "双开": "double open,",
            "单开": "single open,",
            "楼梯": "staircases",
            "已减尺": "size adjusted",
            "二": "second ",
            "一": "first ",
            "或": "or",
            "衣帽间":"Dressing room",
            "对":"face ",
            "窗":" window",
            "韩褶":"pinch ",
            "白":"white ",
            "透":"light filtering ",
            "黑":"black ",
            "灰":"grey ",
            "厨房":"Kitchen",
            "楼":"floor",
            "满墙":"full wall",
            "加":" + ",
            "中间":"middle",
            "中":"middle",
            "临街":"near street ",
            "罗马帘":"Roman blind",
            "客厅":"Living room",
            "侧":" ",
            "旁":" ",
            "拉门":" Sliding door",
            "阳台":"Balcony",
            "遮光":" blackout",
            "大":" large ",
            "双":" double ",
            "透光不透人":"privacy ",
            "厅":"Living room",
            "，":" ",
            "小":"small",
            "楼上":"Upstairs",
            "弯轨":" curved track,"
        }
        
    def translate(self):
        for chinese, english in self.replacements.items():
            self.text = self.text.replace(chinese, english)

        self.text = re.sub(r'(\d+)\s*([wh])', r'\1\2', self.text)
            
        return self.text

    
class Calculation:
    def __init__(self, text):
        self.text = text
        self.w = re.findall(r'(\d+(?:\.\d+)?)w', self.text)
        self.h = re.findall(r'(\d+(?:\.\d+)?)h', self.text)

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h
      
    def vws(self, w, h, x):
        y = 0
        m = 0
        extra = 0
        
        if x == 's':
            y = math.ceil((w * 2.5)/2.8)
        if x == 'p':
            y = math.ceil((w*2.2)/2.8)

        if 3 <= h <= 4:
            extra = 100
        elif 4 < h <= 5:
            extra = 200
        elif h > 5:
            extra = 300

        m = y*(h + 0.3)
        price = math.floor(m*90+extra)
        
        return price

    def vwc(self, w, h, x):
        y = 0
        m = 0
        extra = 0
        
        if x == 's':
            y = math.ceil((w * 2.5)/2.8)
        if x == 'p':
            y = math.ceil((w*2.2)/2.8)

        if 3 <= h <= 4:
            extra = 100
        elif 4 < h <= 5:
            extra = 200
        elif h > 5:
            extra = 300

        m = y*(h + 0.3)
        mini = math.floor(m*110+extra)
        medi = math.floor(m*120+extra)
        maxi = math.floor(m*130+extra)
        maxii = math.floor(m*160+extra)
        
        return f"${mini}, ${medi}, ${maxi}, ${maxii}"

    def ss(self, w):
        mini = 0
        maxi = math.floor(w*2.5*90)
        if w <= 3:
            mini = 450
        elif 3 < w <= 4:
            mini = 650
        elif 4 < w <= 6:
            mini = 900
        
        return f"{mini} ~ {maxi}"

    def sp(self, w):
        mini = 0
        maxi = math.floor(w*2.2*90)
        if w <= 3:
            mini = 450
        elif 3 < w <= 4:
            mini = 650
        elif 4 < w <= 6:
            mini = 900 
        
        return f"{mini} ~ {maxi}"
            
    def rb(self, w, h):
        if w <= 1000:
            w = 1000
        if h <= 1000:
            h = 1000
        
        price = math.floor(w*h*110*0.000001)
        return price

    def sf(self, w, h):
        return math.floor(w*h*380)

    def sn(self, w, h):
        return math.floor(w*h*580)

    def cp(self, w):
        mini = math.floor(w*2.2*110)
        medi = math.floor(w*2.2*120)
        maxi = math.floor(w*2.2*130)
        maxii = math.floor(w*2.2*160)
        return f"${mini}, ${medi}, ${maxi}, ${maxii}"

    def cs(self, w):
        mini = math.floor(w*2.5*110)
        medi = math.floor(w*2.5*120)
        maxi = math.floor(w*2.5*130)
        maxii = math.floor(w*2.5*160)
        return f"${mini}, ${medi}, ${maxi}, ${maxii}"

class CurtainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Curtain Quote")
        self.geometry("800x600")
        self.configure(padx=12, pady=12)

        # Input box
        tk.Label(self, text="输入窗帘描述:").pack(anchor="w")
        self.input_box = tk.Text(self, height=20, wrap="word")
        self.input_box.pack(fill="x", pady=(0, 10))

        # Calculate button
        tk.Button(self, text="翻译/计算", command=self.calculate).pack()

        # Output area (scrollable)
        tk.Label(self, text="Result:").pack(anchor="w", pady=(10, 0))
        self.output = scrolledtext.ScrolledText(self, height=20, wrap="word",
                                              state="disabled")
        self.output.pack(fill="both", expand=True)
        
    def calculate(self):
        # Get input text
        message = self.input_box.get("1.0", tk.END).strip()
        if not message:
            return
            
        # Translate the text
        translator = TranslatorFunc(message)
        translated = translator.translate()
        
        # Split into sections
        sections = re.split(r'\n(?=\S)', translated)
        
        # Prepare output
        output_text = ""
        
        for section in sections:
            section = section.strip()
            if not section:
                continue
                
            # Add the original section
            output_text += f"{section}\n"
            
            # Check if it's a curtain or roller blind section
            dimension = Calculation(section)
            widths = dimension.getWidth()
            heights = dimension.getHeight()
            
            if not widths or not heights:
                continue
                
            w = float(widths[0])
            h = float(heights[0]) if heights else 0
            
            if w >=100:
                # Calculate roller blind price
                roller_blind = dimension.rb(w, h)
                output_text += f"Roller blinds: ${roller_blind} + GST\n"
                if h>=3000:
                    output_text += "卷帘高窗请手动计算"

            elif any(phrase in section.lower() for phrase in ["curtain + sheer", "sheer + curtain"]):
                if h>=3:
                    output_text += "计算高窗：\n"
                    output_text += f"s fold curtain: {dimension.vwc(w,h,'s')} + GST\npinch curtain: {dimension.vwc(w,h,'p')} + GST"
                    output_text += f"\ns fold sheer: ${dimension.vws(w,h,'s')} + GST\npinch sheer: ${dimension.vws(w,h,'p')} + GST"
                else:
                    sheer_s = dimension.ss(w)
                    sheer_p = dimension.sp(w)
                    curtain_s = dimension.cs(w)
                    curtain_p = dimension.cp(w)
                    output_text += f"s fold curtain: {curtain_s} + GST\npinch curtain: {curtain_p} + GST\n"
                    output_text += f"s fold sheer: ${sheer_s} + GST\npinch sheer: ${sheer_p} + GST\n"
            elif "curtain" in section.lower():
                # Calculate curtain prices
                if h>=3:
                    output_text += "计算高窗：\n"
                    output_text += f"s fold curtain: {dimension.vwc(w,h,'s')}\npinch curtain: {dimension.vwc(w,h,'p')}"
                else:
                    curtain_s = dimension.cs(w)
                    curtain_p = dimension.cp(w)
                    output_text += f"s fold curtain: {curtain_s}\npinch curtain: {curtain_p} + GST\n"
            elif "sheer" in section.lower():
                # Calculate sheer prices
                if h>=3:
                    output_text += "计算高窗：\n"
                    output_text += f"s fold sheer: {dimension.vws(w,h,'s')}\npinch sheer: {dimension.vws(w,h,'p')}"
                else:
                    sheer_s = dimension.ss(w)
                    sheer_p = dimension.sp(w)
                    output_text += f"s fold sheer: ${sheer_s} + GST\npinch sheer: ${sheer_p} + GST\n"
            elif w<= 100:
                sheer_s = dimension.ss(w)
                sheer_p = dimension.sp(w)
                curtain_s = dimension.cs(w)
                curtain_p = dimension.cp(w)
                output_text += f"s fold curtain: {curtain_s} + GST\npinch curtain: {curtain_p} + GST\n"
                output_text += f"s fold sheer: ${sheer_s} + GST\npinch sheer: ${sheer_p} + GST\n"
                
            
            output_text += "\n"
        
        # Display output
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", output_text)
        self.output.config(state="disabled")

if __name__ == "__main__":
    app = CurtainApp()
    app.mainloop()

