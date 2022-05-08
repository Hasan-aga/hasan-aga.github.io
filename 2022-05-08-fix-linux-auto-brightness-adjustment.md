# Fix Linux' Auto Brightness Adjustment

How to prevent Linux from changing the screen brightness of your laptop when you plug it in.

---

![macbook pro on brown wooden table](https://images.unsplash.com/photo-1599299009482-3b5326fc52e4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=Mnw5MDg0MHwwfDF8c2VhcmNofDF8fExhcHRvcCUyMGxpbnV4fGVufDB8fHx8MTY1MjAzNDgwMg&ixlib=rb-1.2.1&q=80&w=1080 "Vinayak Sharma")

## The Problem With Linux Screen Brightness Adjustment

I use Ubuntu, and on my Acer Nitro 5, whenever I plug the laptop to power the brightness gets lowered to 10%. This is wrong since I want the brightness not to be lowered when the laptop is charging. It looks like a bug related to the Linux drivers that many users have.

## The Solution

In a nutshell, the solution is to enable the vendor drivers instead of the ones that come with Linux, or so I understood from [this](https://www.debugpoint.com/2016/10/2-ways-fix-laptop-brightness-problem-ubuntu-linux/) post. Here is what I had to do:

- edited the grub file which is at `/etc/default/grub` by adding `acpi_backlight=vendor` to the end of `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`, so the result looks like this:
  
  ```
  GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor"
  ```

-  I ran `update-grub` command in the terminal and restarted the machine.
