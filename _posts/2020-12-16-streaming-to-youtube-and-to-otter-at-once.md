---
layout: post
title: Captioned video calls AND YouTube streaming - surprisingly hard, but achievable
authors:
- yochannah
image: https://images.unsplash.com/photo-1551817958-c5b51e7b4a33?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80
photos:
  name: Photo by Sara Kurfeß on Unsplash
  url: https://unsplash.com/@stereophototyp
---

Since the beginning of OLS-2, we've been using [Otter.ai](https://otter.ai/) to provide realtime closed captioning of our cohort calls to make them more inclusive of our participants. In the process of developing a more accessible format for OLS's calls, we came across a surprising number of nuances to the different services and options one can choose from. With the help of Kaitlin Stack-Whitney and Malvika Sharan, I put together a [preprint with some guidance based on what we learned](https://10.31219/osf.io/k3bfn), including how to handle Zoom break-out rooms that (currently) don't get captioned at all.

Most OLS calls are recorded and uploaded to YouTube after the event, but occasionally we stream to YouTube in realtime. For example, for the OLS-1 graduation calls in the last round. When we decided to live stream a GitHub training call so others beyond OLS could participate, we discovered that we could choose YouTube Streaming _OR_ Otter.ai streaming, but not both. Thankfully, Cass Gould Van Praag (who did most of the GitHub call hosting) swiftly managed to get Google Slides realtime transcription working, which helped to save the day from an unexpected road bump.

We emailed Otter to see if they had a smarter suggestion for how to tackle this next time - and they did! [Restream.io](https://restream.io/) service (for around $20 USD) allows you to stream to Restream and in turn, you can choose multiple locations to stream simultaneously. For this, you'll need a paid-for Zoom account (any tier) and a Business account for Otter. If you want more than two separate streams you'll need to buy a bigger monthly plan.

To sum up the prerequisites:
- **Zoom**: A paid account of some kind that you have admin access to.
- **Otter**: Otter Business.
- **Restream**: You'll need at least the lowest paid tier.
- **YouTube**: Make sure you have a channel set up that allows live streaming!

Getting the details was a little fiddly, so here are the steps we took to get this working.

1. **In the Zoom web interface:** If you already have Otter set up in Zoom - you'll need to turn it off! You can disable the Otter integration in Zoom by going to the Zoom App Marketplace. If you don't, it will override all the settings for the restream stream, and you will be sad.
2. **Set up the YouTube channel in Restream** Assuming you've set up a paid Restream account, go to Restream and set up your two streams as "Channels". YouTube should be pretty self-explanatory as it has a built-in integration already.
3. **Set up the Otter channel in Restream** Otter is where it gets funky. You'll need to create a "CUSTOM RTMP" channel for Otter (make sure it's a channel, _not_ the streaming software (RTMP) box - we'll be using this second box later). When you do, it'll prompt you for some settings. Set "display name" to "Otter" or something similarly meaningful.
4. **Getting the Otter settings for Restream** To fill out the other two, you'll need to go to the Otter site! Once you're logged into Otter, you'll need to [set up a webinar](https://blog.otter.ai/zoom-webinars/) to get the RTMP settings you need. Note that you don't need to actually RUN a Zoom webinar, nor do you need to have an account capable of doing webinars! This is just to get the settings needed for Restream. Once you have the webinar set up at the correct time and date, you will be given a `streaming URL`, a `streaming key`, and a `live streaming page URL`. Make a note of all three.
5. **In your Restream custom RTMP channel** paste in the streaming URL and the streaming key in the relevant fields and save. _Note that you'll have to update this every time you set up a new Otter webinar, as the links only last for as long as the meeting was set up and 30 minutes before / after the stream._
6. **Make a note of your Restream RTMP settings** Look for the "Streaming software (RTMP)" box that's _not_ in the channels pane, and click on the RTMP settings button. This will show two fields, the `RTMP URL` and `Stream key`. Make note of these two settings, you'll need them in the next step.
7. **Finally, set up Zoom to stream to Restream** The last bit is to log into your Zoom account. Zoom has a nice [guide for these two steps](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service), but here's a summary: 
    - make sure streaming to a custom service is enabled, and then set up the meeting you want to stream FROM, and save it. Once it's saved, at the bottom of the meeting page there will be a space to set up custom streaming.  Click on it, and paste in the fields as follows:
    - in `Stream URL`, paste the `RTMP URL` from step (6) above.
    - in `Stream key`, paste the `Stream key` from step (6)
    - For `Live streaming page URL`, you could paste your YouTube stream URL OR your Otter URL. I'd recommend Otter since people in the Zoom call can already see the video so won't benefit from youtube, so paste in the `live streaming page URL` from step (4).
8. That should be everything! Don't forget you can test the stream half an hour before the official start time you set up in Otter, and you'll need to update the Otter Webinar settings in Restream after the webinar expires.

## Thoughts for later

This was actually quite tricky to set up, but we're glad it was, in fact, possible to do. Some improvements that could make this nicer:

- Built-in Restream settings in Zoom.
- Clearer guidance in Otter. We're all from nerdy tech backgrounds and still found it a challenge to get set up - thankfully the Otter team is really great at support so they answered our questions really fast.
- Long-term Otter links. It's a bit of a pain to have to update the channel link in between each call as the webinar settings expire.

Other than those surmountable issues, it was really nice to be able to set up both streaming services at once - and thanks again to Otter for being so ready to answer all our queries!
