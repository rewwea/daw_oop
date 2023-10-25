from mainwindow import Window

if __name__ == "__main__":

    handle = Window()
    handle2 = Window()

    handle.title('Daw')
    handle2.title('Daw2')

    handle.geometry('1280x720')
    handle2.geometry('640x480')

    handle.mainloop()
    handle2.mainloop()
