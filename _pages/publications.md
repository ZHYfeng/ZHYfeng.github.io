---
layout: archive
permalink: /publications/
author_profile: true
title: "Publications"
redirect_from:
  - /publications.html
---

{% if site.author.googlescholar %}
<p>You can also find my articles on <a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.</p>
{% endif %}

<ol class="publist">
  {% for pub in site.data.publications.publications %}
  {% include pub-entry.html pub=pub full=true %}
  {% endfor %}
</ol>
