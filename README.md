# Excluding Googlebot From Abandoned Cart Emails

### Background
Shopify store owners have [been debating for months](https://community.shopify.com/c/Shopify-Discussion/John-Smith-From-Google-UTM-Google-Shopper-Creating-false/td-p/538519) who is behind a flood of abandoned carts that appear to originate from Google.

All of the abandoned carts use the name John Smith, a variety of gmail addresses, the address and phone number for Google Headquarters, and come from an IP address affiliated with Google.

The [Wall Street Journal](https://www.wsj.com/articles/who-is-the-mystery-shopper-leaving-behind-all-those-online-shopping-carts-11593617464) finally settled the debate when Google officially claimed responsibility for the bot.

### Why It Matters
Many ecommerce stores automatically send emails to shoppers who abandon their cart. This is so common in ecommerce that Shopify has a built-in feature for sending them. The John Smith email addresses are not valid, so all of these emails will bounce. Sending emails that bounce can harm your sender reputation and impact deliverability for ALL of your emails.

In addition, many email service providers - like Klaviyo - charge by the profile. By creating additional profiles, the Googlebot can inflate your monthly email marketing bill.

### What To Do About It
You can suppress or remove the Googlebot email addresses as they appear in your store, but that approach has two downsides:

- It requires ongoing maintenance to add new emails to your suppression list as they appear in your store.
- It will not prevent sending abandoned cart notifications the first time a new email is used in your store.

Suppressing all possible Googlebot email addresses at once is the better approach. It requires no ongoing maintenance and will prevent sending any automated emails to invalid addresses.

But how can we know all possible Googlebot email addresses?

We can't know for sure every possible email address that Google uses when crawling stores, but we can take a pretty good guess.

I looked at data from my own store and found 331 unique John Smith email addresses that came from the Googlebot. All of them consisted of a gmail address made of a name followed by a number. I found four different values for the name (johnsmithus, john.smithus, johnsmith.us, and john.smith.us) and every number from 0 to 98. We have never seen a number with three or more digits. Interestingly, we have never seen the number 99 either.

Based on this information, we can guess that Google pulls from a list of 396 possible email addresses (or 400 if 99 is included).

### How To Exclude All Possible Googlebot Email Addresses
We use Klaviyo as our email service provider. These instructions are specific to Klaviyo, but you should be able to adapt them for most ESPs.

1. Download [the CSV of all possible Googlebot email addresses](googlebot-email-address.csv) from this repo.
2. Upload the CSV to the [Suppressed Profiles list in your Klaviyo account](https://www.klaviyo.com/people/suppressed) using the "Upload File" option.

That's it!

## Frequently Asked Questions
#### Why can't I just delete the Googlebot profiles from Klaviyo entirely?
If you delete the profiles completely, Klaviyo will eventually re-sync them from Shopify and recreate the profiles. This will temporarily lower your profile count (and potentially your monthly bill), but it is only a temporary fix.
#### Can't I just create a segment of Googlebot emails and exclude them from my email campaigns?
Yes, you can. Doing so will prevent you from sending emails to these invalid addresses. However, you will have to add flow filters to each of your automated email series and exclude them from every campaign, forever. This is both time-consuming and error-prone. You will still have active profiles for those addresses and potentially inflate your monthly bill.
#### Isn't it possible that some bad actor is disguising their traffic as the Googlebot to crawl my store?
Unfortunately yes, bad actors can use the fact that most ecommerce stores do not block the Googlebot to crawl your store. Attempting to block the Googlebot has the potential to harm your ability to rank in organic search results or advertise on Google Shopping. You will have to decide for yourself if cutting off those traffic sources is worth it. 