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
<img class="img-responsive img-circle cv-pic" src="../static/image/2014-10-05-me-head-100x100.jpg" />
</div>
</div>

## Industry
<hr>

{% for item in industry %}
**{{ item.company }}** <span class="pull-right">{{ item.location }}</span><br />
{% for position in item.positions %}
{{ position.title }} <span class="pull-right">{{ position.dates }}</span><br />
{% endfor %}

{% if item.details %}
{% for detail in item.details %}
{% if detail is string %}
* {{ detail }}
{% else %}
{% for subdetail in detail %}
  * {{ subdetail }}
{% endfor %}
{% endif %}

{% endfor %}
{% endif %}
{% if not loop.last %}
<br />
{% endif %}
{% endfor %}

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

## Education
<hr>

{% for item in education %}
**{{ item.school }}** <span class="pull-right">{{ item.date }}</span><br />
{{ item.degree }} {{ item.gpa }}.<br />

{% if item.details %}
{% for detail in item.details %}
* {{ detail }}
{% endfor %}
{% endif %}
<br />
{% endfor %}

## Skills
<hr>

{% for item in skills %}
**{{ item.type }}:** {{ item.details }}
<br />
{% if not loop.last %}
<br />
{% endif %}
{% endfor %}

## Certificates
<hr>

{% for item in certificates %}
**{{ item.name }}** <span class="pull-right">{{ item.date }}</span>
{% endfor %}

</div>