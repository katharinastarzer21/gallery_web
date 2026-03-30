# Openstack

We are happy to announce that our new OpenStack environment [EODC Cloud](https://cloud.eodc.eu) has launched!

<div id="gallery" style="display:flex;flex-direction:column;gap:20px;max-width:900px;">
<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/openstack/openstack_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Openstack General</strong><br>
    <div style="margin:4px 0 8px 0;">Short general introduction on Openstack, Images, flavors, ...</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="general.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/openstack/openstack_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Openstack Starting</strong><br>
    <div style="margin:4px 0 8px 0;">Description on how to start with the Openstack service.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="openstack_starting.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/openstack/openstack_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Loadbalancers</strong><br>
    <div style="margin:4px 0 8px 0;">How to create a load balancer to distribute network traffic between two instances.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="loadbalancers.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;margin-bottom:20px">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/openstack/openstack_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Distributions</strong><br>
    <div style="margin:4px 0 8px 0;">Learn about our distributions available in Openstack</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="distributions.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>


There are certain things that need to be clarified and explained before you can go ahead and start using your resources on our new infrastructure. OpenStack is an open-source cloud operating system consisting of various components which handle virtualised compute resources. We use an OpenStack environment for the cloud infrastructure service to provide resources to our users.


In order to work with your cloud infrastructure, we will set up an OpenStack "tenant" with a unique identiifer for your company or your project.
In OpenStack, a tenant is a logical group of users and resources that are isolated from other tenants. Each tenant has its own set of users, who can launch virtual machines, manage networks and storage resources.
Please contact us first for an individual offer via office@eodc.eu. After finding a suitable package for you and once your tenant is setup, please create an EODC account following [this](eodc.eu/register) link. Upon confirmation the EODC OpenStack [launcher](https://launcher.eodc.eu/auth/login/?next=/) will give you full control over your resources.

Accessing your tenant is either possible via the [OpenStack Dashboard](https://docs.openstack.org/horizon/latest/user/index.html) or via the [OpenStack API](https://docs.openstack.org/api-quick-start/). <br>
As a preview, you can see how the Dashboard looks like below:

![Openstack Dashboard](../../_static/openstack/openstackDashboard.png)
