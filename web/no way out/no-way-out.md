# LIT CTF 2026 - No Way Out Write-Up - Web

> Author: C0DET1GER

**Challenge Description:**

I made a google form for fun! Check it out:

[https://forms.gle/kniocxKJN1RiDaTU7](https://forms.gle/kniocxKJN1RiDaTU7)

## Solution

**Step 1:**

We see a page asking for the first part of the flag. By inspecting the page, we see in ```FB_PUBLIC_LOAD_DATA_``` we can see the first part of the flag, which is **LITCTF{y0u_**.

<img width="1965" height="610" alt="image" src="https://github.com/user-attachments/assets/3950e67f-3976-4b7f-b997-e087ae1b52e3" />

Text:

```var FB_PUBLIC_LOAD_DATA_ = [null,["Can you complete the form?",[[319529360,"What's the first part of the flag?",null,0,[[685493766,null,1,null,[[2,100,["LITCTF{y0u_"],"nope, that's wrong"]]]],```

**Step 2:**

Next, we see a page asking for the next letters of the flag. By looking at ```FB_PUBLIC_LOAD_DATA_``` again, we can see that only one of the options leads to ```1527147756```, which is the question for the second letter. All the other options lead to ```588010028```, which is back to the first page.  Therfore, we just have to find this option, and then that is our answer.

```[[569456194,[["a",null,588010028,null,0],["b",null,588010028,null,0],["c",null,588010028,null,0],["d",null,588010028,null,0],["e",null,588010028,null,0],["f",null,588010028,null,0],["g",null,588010028,null,0],["h",null,588010028,null,0],["i",null,588010028,null,0],["j",null,588010028,null,0],["k",null,588010028,null,0],["l",null,588010028,null,0],["m",null,588010028,null,0],["n",null,588010028,null,0],["o",null,588010028,null,0],["p",null,588010028,null,0],["q",null,588010028,null,0],["r",null,588010028,null,0],["s",null,588010028,null,0],["t",null,588010028,null,0],["u",null,588010028,null,0],["v",null,588010028,null,0],["w",null,588010028,null,0],["x",null,588010028,null,0],["y",null,588010028,null,0],["z",null,588010028,null,0],["0",null,588010028,null,0],["1",null,588010028,null,0],["2",null,588010028,null,0],["3",null,1527147756,null,0],["4",null,588010028,null,0],["5",null,588010028,null,0],["6",null,588010028,null,0],["7",null,588010028,null,0],["8",null,588010028,null,0],["9",null,588010028,null,0]],1,null,null,null,null,null,0]],null,null,null,null,null,null,[null,"What's the next letter of the flag (1/7)"]]```

We have to repeat that for each of the 7 characters in the section. By finding the one with the number that doesn't lead to ```588010028``` we can get the next letter.

Here are the letters:
1. 3
2. s
3. c
4. 4
5. p
6. e
7. d

Combining this gives **3sc4ped**.

**Step 3:**

Unfortunately, when we go to the next page, it says ```You're trapped here. You can still access the past, but not the future.``` This gives us a hint that we must go to the next part by going back.

In Google Forms, there is an element called ```pageHistory``` which stores your history. Currently, your history has a ```value="0,1,2,3,4,5,6,7,8"```. If you edit it to ```value="0,1,2,3,4,5,6,7,8,9,10"``` and then go back, you can successfully go to page 9, which is the next page.

<img width="1971" height="793" alt="image" src="https://github.com/user-attachments/assets/d5490d50-9d3c-462a-8c7c-9d21f4de9d64" />

After this, we get the rest of the flag, which comes in the following parts:
1. \_th3_f0rm_
2. 6b
3. q3
4. }

After this, we have to combine all the parts of the flag to get **LITCTF{y0u_3sc4ped_th3_f0rm_6bq3}  **

## Summary:
1. Inspect FB_PUBLIC_LOAD_DATA_ to get ```LITCTF{y0u_```
2. Inspect FB_PUBLIC_LOAD_DATA_ and find the correct letter to get ```3sc4ped```
3. Edit pageHistory and go back to get ```_th3_f0rm_6bq3}```

Flag: **LITCTF{y0u_3sc4ped_th3_f0rm_6bq3}**
