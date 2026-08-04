# LIT CTF 2026 - Extremely Original Write-Up - Cryptography

> Author: Ninjaprime

**Challenge Description:**

My flag seems to have been scattered across YouTube! Can you find it and piece it together for me? Starting link: [https://youtu.be/wKz32opINzo](https://youtu.be/wKz32opINzo)

## Solution

**Quest 1:**
> Link: [https://youtu.be/wKz32opINzo](https://youtu.be/wKz32opINzo)

Looking at the video, we see a pipe maze, and after solving it, we see color orange is the correct answer.
<img width="973" height="981" alt="Screenshot 2026-08-03 140159" src="https://github.com/user-attachments/assets/459cdbf1-7feb-4303-a392-4a175241a087" />

Looking at the description of the video, we see hidden text, and since orange is the correct answer, we record **bUB**.
<img width="1807" height="639" alt="image" src="https://github.com/user-attachments/assets/5ce4a302-3b9f-40ac-851a-961dc3235a28" />
```
Lorem ipsum dolor sit amet...
Red: qxU
Orange: bUB
Yellow: sGd
Green: bPA
Blue: mrT
Purple: MTa
Pink: Q==
```
There is hidden text leading to the link for the next quest in the subtitles:
<img width="1767" height="1003" alt="Screenshot 2026-08-03 140143" src="https://github.com/user-attachments/assets/073fe653-55a1-4fe9-bcca-ce232442859c" />

**Quest 2:**
> Link: [https://youtu.be/p1OGNSLqnZI](https://youtu.be/p1OGNSLqnZI)

By switching our subtitles to English (United States) instead of English, we see the hidden text **TdD**.

<img width="1806" height="1145" alt="image" src="https://github.com/user-attachments/assets/2923b948-e59d-4b8c-ae19-a60fb5b04cc7" />

Additionally, by trying the links shown in the video, we see that the third link leads us to Quest 3.

<img width="1801" height="1049" alt="image" src="https://github.com/user-attachments/assets/065584d6-e665-4b31-9c65-7ab70e393313" />

**Quest 3:**
> Link: [https://www.youtube.com/watch?v=Vjf_5VHYy3w](https://www.youtube.com/watch?v=Vjf_5VHYy3w)

Around 6 seconds, we see the gray hidden text **NyM**.

<img width="1784" height="1016" alt="Screenshot 2026-08-03 140306" src="https://github.com/user-attachments/assets/77fee558-177a-43fa-a8ef-6d567a67194f" />

Also, by scrolling down in the description, we find the link to Quest 4.

<img width="1805" height="1216" alt="image" src="https://github.com/user-attachments/assets/4e9cedc8-e9d8-4536-b724-a8736b3f5c28" />


**Quest 4:**
> Link: [https://www.youtube.com/watch?v=znqPQdxS_8U](https://www.youtube.com/watch?v=znqPQdxS_8U)

By looking in the description, we see the text **TAx**.

When the video loads, you see a black screen with a link, but it disappears. You can use a tool like [YouTube Thumbnail Grabber](https://youtube-thumbnail-grabber.com/) to get the next link.

<img width="494" height="402" alt="image" src="https://github.com/user-attachments/assets/844b4ba2-ee32-4e2c-a530-63cbc6d65a6d" />

**Quest 5:**
> Link: [https://youtu.be/bZjgdbGZIEM](https://youtu.be/bZjgdbGZIEM)

In the video, you hear a lot of beeping sounds, which is Morse Code. You can use a tool like [https://myleads.fr/](https://myleads.fr/) to get the audio and then put it into [https://morsecode.world/labs/decoder/](https://morsecode.world/labs/decoder/) to decode it.

We get ```https://youtu.be/r3x8smcuqzk``` when you convert it all to lowercase, but it is wrong.

In the description, we see:
<img width="1828" height="540" alt="image" src="https://github.com/user-attachments/assets/85e7e661-b022-4720-96a6-0691b736261f" />

```
↑
↓
↑
↑
↑
↑
↑
↓
↓
```

This is the case of the link, meaning the first letter is uppercase, the second is lowercase, etc., so the correct link should be: ```https://youtu.be/R3x8SMCUQzk```. But this failed, so then I tried appending ```R3x8SMCUQzk``` directly to ```https://www.youtube.com/watch?v=``` and it worked. 
So the link is: [https://www.youtube.com/watch?v=R3x8SMCUQzk](https://www.youtube.com/watch?v=R3x8SMCUQzk).

**Quest 6:**
> Link: [https://www.youtube.com/watch?v=R3x8SMCUQzk](https://www.youtube.com/watch?v=R3x8SMCUQzk)

In this video, it is revealed that the first part of the flag is **LITCTF{y0uTuB3**.
<img width="752" height="146" alt="image" src="https://github.com/user-attachments/assets/de67910c-bc39-4448-a8b7-f82c4b47eaaa" />

It also says that the flag got scattered throughout the videos and shows a black screen with ```==``` at around 12 seconds.
<img width="443" height="271" alt="image" src="https://github.com/user-attachments/assets/f0d11cd1-bf63-47c1-84e9-206635540610" />

This strongly hints at base64. By combining the first 4 parts, we get **bUBTdDNyMTAx**, which base64 decodes to **m@St3r101**. You can use a tool like [base64decode.org](https://www.base64decode.org/). You can also run the following command in linux:

```bash
echo "bUBTdDNyMTAx" | base64 -d
m@St3r101
```

By combining the parts and adding a closing curly brace, we get the flag: **LITCTF{y0uTuB3m@St3r101}**

## Summary:

| Link | Flag Part | Path to Next |
|---|---|---|
| [Quest 1](https://youtu.be/wKz32opINzo) | bUB | In Subtitles |
| [Quest 2](https://youtu.be/p1OGNSLqnZI) | TdD | Find Correct Link in Video |
| [Quest 3](https://www.youtube.com/watch?v=Vjf_5VHYy3w) | NyM | In Description |
| [Quest 4](https://www.youtube.com/watch?v=znqPQdxS_8U) | TAx | In Thumbnail |
| [Quest 5](https://youtu.be/bZjgdbGZIEM) | N/A | Morse Code + Description for Case |
| [Quest 6](https://www.youtube.com/watch?v=R3x8SMCUQzk) | LITCTF{y0uTuB3 | N/A |

Final Flag: **LITCTF{y0uTuB3m@St3r101}**
