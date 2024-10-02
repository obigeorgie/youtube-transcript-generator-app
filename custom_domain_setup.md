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
