---
layout: default
title: CV
---

{::options parse_block_html="true" /}
<div class="cv">
{% raw %}
<div class="text-center">
# Devon Walker
[PDF](/static/page/cv/Devon-Walker-Resume.pdf)
&#124;
[source](https://github.com/devonwa/latex-resume/blob/master/Walker%2C%20Devon%20-%20Resume.tex)
&#124;
<a href="mailto:{% include email.html %}">{% include email.html %}</a>
&#124;
<a href="https://www.linkedin.com/in/devonwalker">LinkedIn</a>
<br />
</div>
{% endraw %}

## Education

{% for item in education %}
**{{ item.school }}** <span class="pull-right">{{ item.date }}</span><br />
{{ item.degree }}<br />

{% if item.details %}
{% for detail in item.details %}
* {{ detail }}
{% endfor %}
{% endif %}
<br />
{% endfor %}

## Research

{% for item in research %}
**{{ item.name }}** <span class="pull-right">{{ item.location }}</span><br />
_{{ item.title }}_ <span class="pull-right">{{ item.dates }}</span><br />

{% if item.details %}
{% for detail in item.details %}
* {{ detail }}
{% endfor %}
{% endif %}
<br />
{% endfor %}

## Industry

{% for item in industry %}
**{{ item.company }}** <span class="pull-right">{{ item.location }}</span><br />
_{{ item.title }}_ <span class="pull-right">{{ item.dates }}</span><br />

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

## Certificates

{% for item in certificates %}
**{{ item.name }}** <span class="pull-right">{{ item.date }}</span>
{% endfor %}

## Skills

{% for item in skills %}
**{{ item.type }}** -- {{ item.details }}
<br />
{% if not loop.last %}
<br />
{% endif %}
{% endfor %}

## Affiliations

{% for item in affiliations %}
**{{ item.organization }}** <span class="pull-right">{{ item.title }}, {{ item.dates }}</span>
<br />
{% endfor %}
</div>
