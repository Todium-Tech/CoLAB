from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast(
    "Belgin Android", # This is the heading 
    "This is Some Sample Text To Be Shown In The Description", # It is The Description Part
    duration=5, # Its the Number Of Seconds The Toast To Be Displayed
    threaded=True # Wait for Treaded Notification To Finish
)