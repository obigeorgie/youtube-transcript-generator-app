# Setting up a Custom Domain for Your YouTube Transcript Generator

Follow these steps to set up a custom domain for your YouTube Transcript Generator hosted on Replit:

1. **Purchase a domain name**: 
   - Choose a domain registrar (e.g., GoDaddy, Namecheap, Google Domains) and purchase your desired domain name.

2. **Set up DNS records**:
   - Log in to your domain registrar's dashboard.
   - Locate the DNS management section.
   - Add the following DNS records:
     - Type: A
     - Name: @ (or leave blank)
     - Value: 34.110.220.181
     - TTL: 3600 (or 1 hour)

3. **Configure your Replit project**:
   - Open your Replit project.
   - Click on the "Tools" button in the left sidebar.
   - Select "Hosting" from the dropdown menu.
   - In the "Custom domain" section, enter your domain name (e.g., yourdomain.com).
   - Click "Add custom domain".

4. **Verify domain ownership**:
   - Replit will provide you with a TXT record to add to your DNS settings.
   - Go back to your domain registrar's DNS management section.
   - Add a new TXT record with the provided value.
   - Wait for the DNS changes to propagate (this can take up to 24 hours).

5. **Enable HTTPS**:
   - Once your domain is verified, Replit will automatically provision an SSL certificate for your custom domain.
   - This process may take a few minutes to complete.

6. **Update your application**:
   - If your application has any hardcoded URLs or references to the Replit domain, update them to use your new custom domain.

7. **Test your custom domain**:
   - Once the DNS changes have propagated and the SSL certificate is provisioned, visit your custom domain in a web browser.
   - Verify that your YouTube Transcript Generator is accessible and functioning correctly.

Note: It may take up to 24 hours for DNS changes to fully propagate. If you encounter any issues, please check your DNS settings and ensure that you've followed all steps correctly.

Congratulations! Your YouTube Transcript Generator should now be accessible via your custom domain.

# Setting up a Custom Domain with Cloudflare

If you prefer to use Cloudflare for managing your DNS and adding an extra layer of security, follow these steps:

1. **Sign up for Cloudflare**:
   - Go to https://www.cloudflare.com/ and create an account if you don't have one.
   - Once logged in, click on "Add a Site" and enter your domain name.

2. **Update nameservers**:
   - Cloudflare will provide you with two nameservers.
   - Go to your domain registrar's dashboard and update the nameservers to the ones provided by Cloudflare.
   - This step may take up to 24 hours to propagate.

3. **Configure DNS records in Cloudflare**:
   - In your Cloudflare dashboard, go to the "DNS" tab.
   - Add an A record:
     - Type: A
     - Name: @ (or leave blank for root domain)
     - IPv4 address: 34.110.220.181
     - Proxy status: Proxied (orange cloud icon)

4. **Set up SSL/TLS**:
   - In your Cloudflare dashboard, go to the "SSL/TLS" tab.
   - Set the SSL/TLS encryption mode to "Full" or "Full (strict)".

5. **Configure your Replit project**:
   - Follow steps 3-4 from the general instructions above to add your custom domain to your Replit project.

6. **Verify domain ownership**:
   - Add the TXT record provided by Replit to your Cloudflare DNS settings:
     - Type: TXT
     - Name: @ (or as specified by Replit)
     - Content: (the verification string provided by Replit)
     - Proxy status: DNS only (gray cloud icon)

7. **Enable HTTPS in Replit**:
   - Wait for Replit to verify your domain ownership and provision the SSL certificate.

8. **Update your application**:
   - If necessary, update any hardcoded URLs in your application to use your new custom domain.

9. **Test your custom domain**:
   - Visit your custom domain in a web browser and verify that your YouTube Transcript Generator is accessible and functioning correctly.
   - Check that HTTPS is working properly.

10. **Optional: Enable Cloudflare features**:
    - Explore Cloudflare's security features like Web Application Firewall (WAF) and DDoS protection.
    - Consider enabling Cloudflare's performance features like caching and minification for better site performance.

Note: When using Cloudflare, DNS propagation is usually faster, but it may still take some time for all changes to take effect globally.

By following these steps, you'll have set up your custom domain with Cloudflare, adding an extra layer of security and performance to your YouTube Transcript Generator.
