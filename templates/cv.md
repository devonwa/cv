---
layout: default
title: CV
---

{::options parse_block_html="true" /}
<div class="cv">
<div class="row">
<div class="col-xs-8">
<div class="text-left">
# {{ info.name }}
[PDF](/static/page/cv/Devon-Walker-Resume.pdf)
&#124;
[source](https://github.com/devonwa/cv)
&#124;
{% raw %}
<a href="mailto:{% include email.html %}">{% include email.html %}</a>
{% endraw %}
<br />
<br />
</div>
</div>
<div class="col-xs-4">
<img class="img-responsive img-circle cv-pic" src="../static/image/profile_pic.png" />
</div>
</div>


## Skills
<hr>

{% for item in skills %}
**{{ item.type }}:** {{ item.details }}<br />
{% endfor %}


## Experience
<hr>

{% for item in industry %}
**{{ item.company }}** <span class="pull-right">{{ item.location }}</span><br />
{% for position in item.positions %}
<i>{{ position.title }} <span class="pull-right">{{ position.dates }}</span></i><br />
{% if position.details %}
{% for detail in position.details %}
* <b>{{ detail.topic }}</b>: {{ detail.summary }}
{% endfor %}
<br />
{% endif %}

{% endfor %}


{% if not loop.last %}
<br />
{% endif %}


{% endfor %}

<!-- 
## Research
<hr>

{% for item in research %}
**{{ item.name }}** <span class="pull-right">{{ item.location }}</span><br />
{{ item.title }} <span class="pull-right">{{ item.dates }}</span><br />
{% for p in item.project %}
{{ p.title }}

{% if p.details %}
{% for detail in p.details %}
* {{ detail }}
{% endfor %}
{% else %}
{% endif %}
{% endfor %}
<br />
{% endfor %} 
-->

## Education
<hr>

{% for item in education %}
**{{ item.school }}** <span class="pull-right">{{ item.location }}</span><br />
<i>{{ item.degree }} {{ item.gpa }}. <span class="pull-right">{{ item.date }}</span></i><br />
{% if item.minor %}<i>Minor in {{ item.minor }}.</i><br />{% endif %}

{% if item.details %}
{% for detail in item.details %}
* **{{ detail.topic }}**: {{ detail.summary }}
{% endfor %}
{% endif %}

<br />

{% endfor %}

</div>