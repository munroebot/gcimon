<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
 <title>/TV.com/trunk/src/python-test/xmlrunner.py - XBMC - Trac</title><link rel="start" href="/wiki" /><link rel="search" href="/search" /><link rel="help" href="/wiki/TracGuide" /><link rel="stylesheet" href="/trac/css/trac.css" type="text/css" /><link rel="stylesheet" href="/trac/css/code.css" type="text/css" /><link rel="stylesheet" href="/trac/css/browser.css" type="text/css" /><link rel="icon" href="/chrome/common/trac.ico" type="image/x-icon" /><link rel="shortcut icon" href="/chrome/common/trac.ico" type="image/x-icon" /><link rel="up" href="/browser/TV.com/trunk/src/python-test" title="Parent directory" /><link rel="alternate" href="/browser/TV.com/trunk/src/python-test/xmlrunner.py?format=txt" title="Plain Text" type="text/plain" /><link rel="alternate" href="/browser/TV.com/trunk/src/python-test/xmlrunner.py?format=raw" title="Original Format" type="text/x-python; charset=iso-8859-15" /><style type="text/css">
</style>
 <script type="text/javascript" src="/trac/js/trac.js"></script>
 <script type="text/javascript" src="/chrome/ctxtnavadd/js/ctxtnavadd.js"></script>
</head>
<body>


<div id="banner">

<div id="header"><a id="logo" href="http://xbmc.ramfelt.se"><img src="/chrome/common/trac_banner.png" width="236" height="73" alt="Trac" /></a><hr /></div>

<form id="search" action="/search" method="get">
 <div>
  <label for="proj-search">Search:</label>
  <input type="text" id="proj-search" name="q" size="10" accesskey="f" value="" />
  <input type="submit" value="Search" />
  <input type="hidden" name="wiki" value="on" />
  <input type="hidden" name="changeset" value="on" />
  <input type="hidden" name="ticket" value="on" />
 </div>
</form>



<div id="metanav" class="nav"><ul><li class="first"><a href="/login">Login</a></li><li><a href="/settings">Settings</a></li><li><a accesskey="6" href="/wiki/TracGuide">Help/Guide</a></li><li class="last"><a href="/about">About Trac</a></li></ul></div>
</div>

<div id="mainnav" class="nav"><ul><li class="first"><a accesskey="1" href="/wiki">Wiki</a></li><li><a href="/downloads">Downloads</a></li><li><a accesskey="3" href="/roadmap">Roadmap</a></li><li><a accesskey="2" href="/timeline">Timeline</a></li><li class="active"><a href="/browser">Browse Source</a></li><li><a href="/report">View Tickets</a></li><li class="last"><a href="/hudson/">Builds</a></li></ul></div>
<div id="main">




<div id="ctxtnav" class="nav">
 <ul>
  <li class="first"><a href="/changeset/296/TV.com/trunk/src/python-test/xmlrunner.py">
   Last Change</a></li>
  <li class="last"><a href="/log/TV.com/trunk/src/python-test/xmlrunner.py">
   Revision Log</a></li>
 </ul>
</div>


<div id="searchable">
<div id="content" class="browser">
 <h1><a class="first" title="Go to root directory" href="/browser">root</a><span class="sep">/</span><a title="View TV.com" href="/browser/TV.com">TV.com</a><span class="sep">/</span><a title="View trunk" href="/browser/TV.com/trunk">trunk</a><span class="sep">/</span><a title="View src" href="/browser/TV.com/trunk/src">src</a><span class="sep">/</span><a title="View python-test" href="/browser/TV.com/trunk/src/python-test">python-test</a><span class="sep">/</span><a title="View xmlrunner.py" href="/browser/TV.com/trunk/src/python-test/xmlrunner.py">xmlrunner.py</a></h1>

 <div id="jumprev">
  <form action="" method="get">
   <div>
    <label for="rev">View revision:</label>
    <input type="text" id="rev" name="rev" value="" size="4" />
   </div>
  </form>
 </div>

 

 
  <table id="info" summary="Revision info"><tr>
    <th scope="col">
     Revision <a href="/changeset/296">296</a>, 11.9 kB
     (checked in by redsolo, 9 months ago)
    </th></tr><tr>
    <td class="message"><p>
Still fixing <a class="closed ticket" href="/ticket/93" title="Integrate into hudson (closed)">#93</a> <br />
</p>
</td>
   </tr>
  </table>
  <div id="preview"><table class="code"><thead><tr><th class="lineno">Line</th><th class="content">&nbsp;</th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th>
<td>&#34;&#34;&#34;</td>
</tr><tr><th id="L2"><a href="#L2">2</a></th>
<td>XML Test Runner for PyUnit</td>
</tr><tr><th id="L3"><a href="#L3">3</a></th>
<td>&#34;&#34;&#34;</td>
</tr><tr><th id="L4"><a href="#L4">4</a></th>
<td></td>
</tr><tr><th id="L5"><a href="#L5">5</a></th>
<td># Written by Sebastian Rittau &lt;srittau@jroger.in-berlin.de&gt; and placed in</td>
</tr><tr><th id="L6"><a href="#L6">6</a></th>
<td># the Public Domain.</td>
</tr><tr><th id="L7"><a href="#L7">7</a></th>
<td></td>
</tr><tr><th id="L8"><a href="#L8">8</a></th>
<td>__revision__ = &#34;$Id: /mirror/jroger/python/stdlib/xmlrunner.py 3506 2006-07-27T09:12:39.629878Z srittau&nbsp; $&#34;</td>
</tr><tr><th id="L9"><a href="#L9">9</a></th>
<td></td>
</tr><tr><th id="L10"><a href="#L10">10</a></th>
<td>import os.path</td>
</tr><tr><th id="L11"><a href="#L11">11</a></th>
<td>import re</td>
</tr><tr><th id="L12"><a href="#L12">12</a></th>
<td>import sys</td>
</tr><tr><th id="L13"><a href="#L13">13</a></th>
<td>import time</td>
</tr><tr><th id="L14"><a href="#L14">14</a></th>
<td>import traceback</td>
</tr><tr><th id="L15"><a href="#L15">15</a></th>
<td>import unittest</td>
</tr><tr><th id="L16"><a href="#L16">16</a></th>
<td>from StringIO import StringIO</td>
</tr><tr><th id="L17"><a href="#L17">17</a></th>
<td>from xml.sax.saxutils import escape</td>
</tr><tr><th id="L18"><a href="#L18">18</a></th>
<td></td>
</tr><tr><th id="L19"><a href="#L19">19</a></th>
<td>from StringIO import StringIO</td>
</tr><tr><th id="L20"><a href="#L20">20</a></th>
<td></td>
</tr><tr><th id="L21"><a href="#L21">21</a></th>
<td></td>
</tr><tr><th id="L22"><a href="#L22">22</a></th>
<td>class _TestInfo(object):</td>
</tr><tr><th id="L23"><a href="#L23">23</a></th>
<td>&nbsp; &nbsp; &#34;&#34;&#34;Information about a particular test.</td>
</tr><tr><th id="L24"><a href="#L24">24</a></th>
<td>&nbsp; &nbsp; </td>
</tr><tr><th id="L25"><a href="#L25">25</a></th>
<td>&nbsp; &nbsp; Used by _XmlTestResult.&#34;&#34;&#34;</td>
</tr><tr><th id="L26"><a href="#L26">26</a></th>
<td>&nbsp; &nbsp; def __init__(self, test, time):</td>
</tr><tr><th id="L27"><a href="#L27">27</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; (self._class, self._method) = test.id().rsplit(&#34;.&#34;, 1)</td>
</tr><tr><th id="L28"><a href="#L28">28</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._time = time</td>
</tr><tr><th id="L29"><a href="#L29">29</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._error = None</td>
</tr><tr><th id="L30"><a href="#L30">30</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._failure = None</td>
</tr><tr><th id="L31"><a href="#L31">31</a></th>
<td></td>
</tr><tr><th id="L32"><a href="#L32">32</a></th>
<td>&nbsp; &nbsp; @staticmethod</td>
</tr><tr><th id="L33"><a href="#L33">33</a></th>
<td>&nbsp; &nbsp; def create_success(test, time):</td>
</tr><tr><th id="L34"><a href="#L34">34</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Create a _TestInfo instance for a successful test.&#34;&#34;&#34;</td>
</tr><tr><th id="L35"><a href="#L35">35</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; return _TestInfo(test, time)</td>
</tr><tr><th id="L36"><a href="#L36">36</a></th>
<td></td>
</tr><tr><th id="L37"><a href="#L37">37</a></th>
<td>&nbsp; &nbsp; @staticmethod</td>
</tr><tr><th id="L38"><a href="#L38">38</a></th>
<td>&nbsp; &nbsp; def create_failure(test, time, failure):</td>
</tr><tr><th id="L39"><a href="#L39">39</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Create a _TestInfo instance for a failed test.&#34;&#34;&#34;</td>
</tr><tr><th id="L40"><a href="#L40">40</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; info = _TestInfo(test, time)</td>
</tr><tr><th id="L41"><a href="#L41">41</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; info._failure = failure</td>
</tr><tr><th id="L42"><a href="#L42">42</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; return info</td>
</tr><tr><th id="L43"><a href="#L43">43</a></th>
<td></td>
</tr><tr><th id="L44"><a href="#L44">44</a></th>
<td>&nbsp; &nbsp; @staticmethod</td>
</tr><tr><th id="L45"><a href="#L45">45</a></th>
<td>&nbsp; &nbsp; def create_error(test, time, error):</td>
</tr><tr><th id="L46"><a href="#L46">46</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Create a _TestInfo instance for an erroneous test.&#34;&#34;&#34;</td>
</tr><tr><th id="L47"><a href="#L47">47</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; info = _TestInfo(test, time)</td>
</tr><tr><th id="L48"><a href="#L48">48</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; info._error = error</td>
</tr><tr><th id="L49"><a href="#L49">49</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; return info</td>
</tr><tr><th id="L50"><a href="#L50">50</a></th>
<td></td>
</tr><tr><th id="L51"><a href="#L51">51</a></th>
<td>&nbsp; &nbsp; def print_report(self, stream):</td>
</tr><tr><th id="L52"><a href="#L52">52</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Print information about this test case in XML format to the</td>
</tr><tr><th id="L53"><a href="#L53">53</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; supplied stream.</td>
</tr><tr><th id="L54"><a href="#L54">54</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L55"><a href="#L55">55</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&nbsp; &lt;testcase classname=&#34;%(class)s&#34; name=&#34;%(method)s&#34; time=&#34;%(time).4f&#34;&gt;' % \</td>
</tr><tr><th id="L56"><a href="#L56">56</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</td>
</tr><tr><th id="L57"><a href="#L57">57</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;class&#34;: self._class,</td>
</tr><tr><th id="L58"><a href="#L58">58</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;method&#34;: self._method,</td>
</tr><tr><th id="L59"><a href="#L59">59</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;time&#34;: self._time,</td>
</tr><tr><th id="L60"><a href="#L60">60</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; })</td>
</tr><tr><th id="L61"><a href="#L61">61</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; if self._failure != None:</td>
</tr><tr><th id="L62"><a href="#L62">62</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; self._print_error(stream, 'failure', self._failure)</td>
</tr><tr><th id="L63"><a href="#L63">63</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; if self._error != None:</td>
</tr><tr><th id="L64"><a href="#L64">64</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; self._print_error(stream, 'error', self._error)</td>
</tr><tr><th id="L65"><a href="#L65">65</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&lt;/testcase&gt;\n')</td>
</tr><tr><th id="L66"><a href="#L66">66</a></th>
<td></td>
</tr><tr><th id="L67"><a href="#L67">67</a></th>
<td>&nbsp; &nbsp; def _print_error(self, stream, tagname, error):</td>
</tr><tr><th id="L68"><a href="#L68">68</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Print information from a failure or error to the supplied stream.&#34;&#34;&#34;</td>
</tr><tr><th id="L69"><a href="#L69">69</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; text = escape(str(error[1]))</td>
</tr><tr><th id="L70"><a href="#L70">70</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('\n')</td>
</tr><tr><th id="L71"><a href="#L71">71</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&nbsp; &nbsp; &lt;%s type=&#34;%s&#34;&gt;%s\n' \</td>
</tr><tr><th id="L72"><a href="#L72">72</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; % (tagname, str(error[0]), text))</td>
</tr><tr><th id="L73"><a href="#L73">73</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; tb_stream = StringIO()</td>
</tr><tr><th id="L74"><a href="#L74">74</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; traceback.print_tb(error[2], None, tb_stream)</td>
</tr><tr><th id="L75"><a href="#L75">75</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write(escape(tb_stream.getvalue()))</td>
</tr><tr><th id="L76"><a href="#L76">76</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&nbsp; &nbsp; &lt;/%s&gt;\n' % tagname)</td>
</tr><tr><th id="L77"><a href="#L77">77</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&nbsp; ')</td>
</tr><tr><th id="L78"><a href="#L78">78</a></th>
<td></td>
</tr><tr><th id="L79"><a href="#L79">79</a></th>
<td></td>
</tr><tr><th id="L80"><a href="#L80">80</a></th>
<td>class _XmlTestResult(unittest.TestResult):</td>
</tr><tr><th id="L81"><a href="#L81">81</a></th>
<td>&nbsp; &nbsp; &#34;&#34;&#34;A test result class that stores result as XML.</td>
</tr><tr><th id="L82"><a href="#L82">82</a></th>
<td></td>
</tr><tr><th id="L83"><a href="#L83">83</a></th>
<td>&nbsp; &nbsp; Used by XmlTestRunner.</td>
</tr><tr><th id="L84"><a href="#L84">84</a></th>
<td>&nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L85"><a href="#L85">85</a></th>
<td>&nbsp; &nbsp; def __init__(self, classname):</td>
</tr><tr><th id="L86"><a href="#L86">86</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; unittest.TestResult.__init__(self)</td>
</tr><tr><th id="L87"><a href="#L87">87</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._test_name = classname</td>
</tr><tr><th id="L88"><a href="#L88">88</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._start_time = None</td>
</tr><tr><th id="L89"><a href="#L89">89</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._tests = []</td>
</tr><tr><th id="L90"><a href="#L90">90</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._error = None</td>
</tr><tr><th id="L91"><a href="#L91">91</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._failure = None</td>
</tr><tr><th id="L92"><a href="#L92">92</a></th>
<td></td>
</tr><tr><th id="L93"><a href="#L93">93</a></th>
<td>&nbsp; &nbsp; def startTest(self, test):</td>
</tr><tr><th id="L94"><a href="#L94">94</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; unittest.TestResult.startTest(self, test)</td>
</tr><tr><th id="L95"><a href="#L95">95</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._error = None</td>
</tr><tr><th id="L96"><a href="#L96">96</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._failure = None</td>
</tr><tr><th id="L97"><a href="#L97">97</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._start_time = time.time()</td>
</tr><tr><th id="L98"><a href="#L98">98</a></th>
<td></td>
</tr><tr><th id="L99"><a href="#L99">99</a></th>
<td>&nbsp; &nbsp; def stopTest(self, test):</td>
</tr><tr><th id="L100"><a href="#L100">100</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; time_taken = time.time() - self._start_time</td>
</tr><tr><th id="L101"><a href="#L101">101</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; unittest.TestResult.stopTest(self, test)</td>
</tr><tr><th id="L102"><a href="#L102">102</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; if self._error:</td>
</tr><tr><th id="L103"><a href="#L103">103</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info = _TestInfo.create_error(test, time_taken, self._error)</td>
</tr><tr><th id="L104"><a href="#L104">104</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; elif self._failure:</td>
</tr><tr><th id="L105"><a href="#L105">105</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info = _TestInfo.create_failure(test, time_taken, self._failure)</td>
</tr><tr><th id="L106"><a href="#L106">106</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; else:</td>
</tr><tr><th id="L107"><a href="#L107">107</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info = _TestInfo.create_success(test, time_taken)</td>
</tr><tr><th id="L108"><a href="#L108">108</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._tests.append(info)</td>
</tr><tr><th id="L109"><a href="#L109">109</a></th>
<td></td>
</tr><tr><th id="L110"><a href="#L110">110</a></th>
<td>&nbsp; &nbsp; def addError(self, test, err):</td>
</tr><tr><th id="L111"><a href="#L111">111</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; unittest.TestResult.addError(self, test, err)</td>
</tr><tr><th id="L112"><a href="#L112">112</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._error = err</td>
</tr><tr><th id="L113"><a href="#L113">113</a></th>
<td></td>
</tr><tr><th id="L114"><a href="#L114">114</a></th>
<td>&nbsp; &nbsp; def addFailure(self, test, err):</td>
</tr><tr><th id="L115"><a href="#L115">115</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; unittest.TestResult.addFailure(self, test, err)</td>
</tr><tr><th id="L116"><a href="#L116">116</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._failure = err</td>
</tr><tr><th id="L117"><a href="#L117">117</a></th>
<td></td>
</tr><tr><th id="L118"><a href="#L118">118</a></th>
<td>&nbsp; &nbsp; def print_report(self, stream, time_taken, out, err):</td>
</tr><tr><th id="L119"><a href="#L119">119</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Prints the XML report to the supplied stream.</td>
</tr><tr><th id="L120"><a href="#L120">120</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; </td>
</tr><tr><th id="L121"><a href="#L121">121</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; The time the tests took to perform as well as the captured standard</td>
</tr><tr><th id="L122"><a href="#L122">122</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; output and standard error streams must be passed in.</td>
</tr><tr><th id="L123"><a href="#L123">123</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L124"><a href="#L124">124</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&lt;testsuite errors=&#34;%(e)d&#34; failures=&#34;%(f)d&#34; ' % \</td>
</tr><tr><th id="L125"><a href="#L125">125</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &#34;e&#34;: len(self.errors), &#34;f&#34;: len(self.failures) })</td>
</tr><tr><th id="L126"><a href="#L126">126</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('name=&#34;%(n)s&#34; tests=&#34;%(t)d&#34; time=&#34;%(time).3f&#34;&gt;\n' % \</td>
</tr><tr><th id="L127"><a href="#L127">127</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</td>
</tr><tr><th id="L128"><a href="#L128">128</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;n&#34;: self._test_name,</td>
</tr><tr><th id="L129"><a href="#L129">129</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;t&#34;: self.testsRun,</td>
</tr><tr><th id="L130"><a href="#L130">130</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;time&#34;: time_taken,</td>
</tr><tr><th id="L131"><a href="#L131">131</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; })</td>
</tr><tr><th id="L132"><a href="#L132">132</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; for info in self._tests:</td>
</tr><tr><th id="L133"><a href="#L133">133</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info.print_report(stream)</td>
</tr><tr><th id="L134"><a href="#L134">134</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&nbsp; &lt;system-out&gt;&lt;![CDATA[%s]]&gt;&lt;/system-out&gt;\n' % out)</td>
</tr><tr><th id="L135"><a href="#L135">135</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&nbsp; &lt;system-err&gt;&lt;![CDATA[%s]]&gt;&lt;/system-err&gt;\n' % err)</td>
</tr><tr><th id="L136"><a href="#L136">136</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; stream.write('&lt;/testsuite&gt;\n')</td>
</tr><tr><th id="L137"><a href="#L137">137</a></th>
<td></td>
</tr><tr><th id="L138"><a href="#L138">138</a></th>
<td></td>
</tr><tr><th id="L139"><a href="#L139">139</a></th>
<td>class XmlTestRunner(object):</td>
</tr><tr><th id="L140"><a href="#L140">140</a></th>
<td>&nbsp; &nbsp; &#34;&#34;&#34;A test runner that stores results in XML format compatible with JUnit.</td>
</tr><tr><th id="L141"><a href="#L141">141</a></th>
<td></td>
</tr><tr><th id="L142"><a href="#L142">142</a></th>
<td>&nbsp; &nbsp; XmlTestRunner(stream=None) -&gt; XML test runner</td>
</tr><tr><th id="L143"><a href="#L143">143</a></th>
<td></td>
</tr><tr><th id="L144"><a href="#L144">144</a></th>
<td>&nbsp; &nbsp; The XML file is written to the supplied stream. If stream is None, the</td>
</tr><tr><th id="L145"><a href="#L145">145</a></th>
<td>&nbsp; &nbsp; results are stored in a file called TEST-&lt;module&gt;.&lt;class&gt;.xml in the</td>
</tr><tr><th id="L146"><a href="#L146">146</a></th>
<td>&nbsp; &nbsp; current working directory (if not overridden with the path property),</td>
</tr><tr><th id="L147"><a href="#L147">147</a></th>
<td>&nbsp; &nbsp; where &lt;module&gt; and &lt;class&gt; are the module and class name of the test class.</td>
</tr><tr><th id="L148"><a href="#L148">148</a></th>
<td>&nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L149"><a href="#L149">149</a></th>
<td>&nbsp; &nbsp; def __init__(self, stream=None):</td>
</tr><tr><th id="L150"><a href="#L150">150</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._stream = stream</td>
</tr><tr><th id="L151"><a href="#L151">151</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._path = &#34;.&#34;</td>
</tr><tr><th id="L152"><a href="#L152">152</a></th>
<td></td>
</tr><tr><th id="L153"><a href="#L153">153</a></th>
<td>&nbsp; &nbsp; def run(self, test):</td>
</tr><tr><th id="L154"><a href="#L154">154</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Run the given test case or test suite.&#34;&#34;&#34;</td>
</tr><tr><th id="L155"><a href="#L155">155</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class_ = test.__class__</td>
</tr><tr><th id="L156"><a href="#L156">156</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; classname = class_.__module__ + &#34;.&#34; + class_.__name__</td>
</tr><tr><th id="L157"><a href="#L157">157</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; if self._stream == None:</td>
</tr><tr><th id="L158"><a href="#L158">158</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filename = &#34;TEST-%s.xml&#34; % classname</td>
</tr><tr><th id="L159"><a href="#L159">159</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stream = file(os.path.join(self._path, filename), &#34;w&#34;)</td>
</tr><tr><th id="L160"><a href="#L160">160</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stream.write('&lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt;\n')</td>
</tr><tr><th id="L161"><a href="#L161">161</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; else:</td>
</tr><tr><th id="L162"><a href="#L162">162</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stream = self._stream</td>
</tr><tr><th id="L163"><a href="#L163">163</a></th>
<td></td>
</tr><tr><th id="L164"><a href="#L164">164</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; result = _XmlTestResult(classname)</td>
</tr><tr><th id="L165"><a href="#L165">165</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; start_time = time.time()</td>
</tr><tr><th id="L166"><a href="#L166">166</a></th>
<td></td>
</tr><tr><th id="L167"><a href="#L167">167</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; # TODO: Python 2.5: Use the with statement</td>
</tr><tr><th id="L168"><a href="#L168">168</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; old_stdout = sys.stdout</td>
</tr><tr><th id="L169"><a href="#L169">169</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; old_stderr = sys.stderr</td>
</tr><tr><th id="L170"><a href="#L170">170</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; sys.stdout = StringIO()</td>
</tr><tr><th id="L171"><a href="#L171">171</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; sys.stderr = StringIO()</td>
</tr><tr><th id="L172"><a href="#L172">172</a></th>
<td></td>
</tr><tr><th id="L173"><a href="#L173">173</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; try:</td>
</tr><tr><th id="L174"><a href="#L174">174</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; test(result)</td>
</tr><tr><th id="L175"><a href="#L175">175</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; try:</td>
</tr><tr><th id="L176"><a href="#L176">176</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; out_s = sys.stdout.getvalue()</td>
</tr><tr><th id="L177"><a href="#L177">177</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; except AttributeError:</td>
</tr><tr><th id="L178"><a href="#L178">178</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; out_s = &#34;&#34;</td>
</tr><tr><th id="L179"><a href="#L179">179</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; try:</td>
</tr><tr><th id="L180"><a href="#L180">180</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; err_s = sys.stderr.getvalue()</td>
</tr><tr><th id="L181"><a href="#L181">181</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; except AttributeError:</td>
</tr><tr><th id="L182"><a href="#L182">182</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; err_s = &#34;&#34;</td>
</tr><tr><th id="L183"><a href="#L183">183</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; finally:</td>
</tr><tr><th id="L184"><a href="#L184">184</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sys.stdout = old_stdout</td>
</tr><tr><th id="L185"><a href="#L185">185</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sys.stderr = old_stderr</td>
</tr><tr><th id="L186"><a href="#L186">186</a></th>
<td></td>
</tr><tr><th id="L187"><a href="#L187">187</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; time_taken = time.time() - start_time</td>
</tr><tr><th id="L188"><a href="#L188">188</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; result.print_report(stream, time_taken, out_s, err_s)</td>
</tr><tr><th id="L189"><a href="#L189">189</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; if self._stream == None:</td>
</tr><tr><th id="L190"><a href="#L190">190</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stream.close()</td>
</tr><tr><th id="L191"><a href="#L191">191</a></th>
<td></td>
</tr><tr><th id="L192"><a href="#L192">192</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; return result</td>
</tr><tr><th id="L193"><a href="#L193">193</a></th>
<td></td>
</tr><tr><th id="L194"><a href="#L194">194</a></th>
<td>&nbsp; &nbsp; def _set_path(self, path):</td>
</tr><tr><th id="L195"><a href="#L195">195</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._path = path</td>
</tr><tr><th id="L196"><a href="#L196">196</a></th>
<td></td>
</tr><tr><th id="L197"><a href="#L197">197</a></th>
<td>&nbsp; &nbsp; path = property(lambda self: self._path, _set_path, None,</td>
</tr><tr><th id="L198"><a href="#L198">198</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;The path where the XML files are stored.</td>
</tr><tr><th id="L199"><a href="#L199">199</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </td>
</tr><tr><th id="L200"><a href="#L200">200</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; This property is ignored when the XML file is written to a file</td>
</tr><tr><th id="L201"><a href="#L201">201</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stream.&#34;&#34;&#34;)</td>
</tr><tr><th id="L202"><a href="#L202">202</a></th>
<td></td>
</tr><tr><th id="L203"><a href="#L203">203</a></th>
<td></td>
</tr><tr><th id="L204"><a href="#L204">204</a></th>
<td>class XmlTestRunnerTest(unittest.TestCase):</td>
</tr><tr><th id="L205"><a href="#L205">205</a></th>
<td>&nbsp; &nbsp; def setUp(self):</td>
</tr><tr><th id="L206"><a href="#L206">206</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._stream = StringIO()</td>
</tr><tr><th id="L207"><a href="#L207">207</a></th>
<td></td>
</tr><tr><th id="L208"><a href="#L208">208</a></th>
<td>&nbsp; &nbsp; def _try_test_run(self, test_class, expected):</td>
</tr><tr><th id="L209"><a href="#L209">209</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Run the test suite against the supplied test class and compare the</td>
</tr><tr><th id="L210"><a href="#L210">210</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; XML result against the expected XML string. Fail if the expected</td>
</tr><tr><th id="L211"><a href="#L211">211</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; string doesn't match the actual string. All time attribute in the</td>
</tr><tr><th id="L212"><a href="#L212">212</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; expected string should have the value &#34;0.000&#34;. All error and failure</td>
</tr><tr><th id="L213"><a href="#L213">213</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; messages are reduced to &#34;Foobar&#34;.</td>
</tr><tr><th id="L214"><a href="#L214">214</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L215"><a href="#L215">215</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner = XmlTestRunner(self._stream)</td>
</tr><tr><th id="L216"><a href="#L216">216</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner.run(unittest.makeSuite(test_class))</td>
</tr><tr><th id="L217"><a href="#L217">217</a></th>
<td></td>
</tr><tr><th id="L218"><a href="#L218">218</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; got = self._stream.getvalue()</td>
</tr><tr><th id="L219"><a href="#L219">219</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; # Replace all time=&#34;X.YYY&#34; attributes by time=&#34;0.000&#34; to enable a</td>
</tr><tr><th id="L220"><a href="#L220">220</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; # simple string comparison.</td>
</tr><tr><th id="L221"><a href="#L221">221</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; got = re.sub(r'time=&#34;\d+\.\d+&#34;', 'time=&#34;0.000&#34;', got)</td>
</tr><tr><th id="L222"><a href="#L222">222</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; # Likewise, replace all failure and error messages by a simple &#34;Foobar&#34;</td>
</tr><tr><th id="L223"><a href="#L223">223</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; # string.</td>
</tr><tr><th id="L224"><a href="#L224">224</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; got = re.sub(r'(?s)&lt;failure (.*?)&gt;.*?&lt;/failure&gt;', r'&lt;failure \1&gt;Foobar&lt;/failure&gt;', got)</td>
</tr><tr><th id="L225"><a href="#L225">225</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; got = re.sub(r'(?s)&lt;error (.*?)&gt;.*?&lt;/error&gt;', r'&lt;error \1&gt;Foobar&lt;/error&gt;', got)</td>
</tr><tr><th id="L226"><a href="#L226">226</a></th>
<td></td>
</tr><tr><th id="L227"><a href="#L227">227</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self.assertEqual(expected, got)</td>
</tr><tr><th id="L228"><a href="#L228">228</a></th>
<td></td>
</tr><tr><th id="L229"><a href="#L229">229</a></th>
<td>&nbsp; &nbsp; def test_no_tests(self):</td>
</tr><tr><th id="L230"><a href="#L230">230</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Regression test: Check whether a test run without any tests</td>
</tr><tr><th id="L231"><a href="#L231">231</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; matches a previous run.&#34;&#34;&#34;</td>
</tr><tr><th id="L232"><a href="#L232">232</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L233"><a href="#L233">233</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pass</td>
</tr><tr><th id="L234"><a href="#L234">234</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._try_test_run(TestTest, &#34;&#34;&#34;&lt;testsuite errors=&#34;0&#34; failures=&#34;0&#34; name=&#34;unittest.TestSuite&#34; tests=&#34;0&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L235"><a href="#L235">235</a></th>
<td>&nbsp; &lt;system-out&gt;&lt;![CDATA[]]&gt;&lt;/system-out&gt;</td>
</tr><tr><th id="L236"><a href="#L236">236</a></th>
<td>&nbsp; &lt;system-err&gt;&lt;![CDATA[]]&gt;&lt;/system-err&gt;</td>
</tr><tr><th id="L237"><a href="#L237">237</a></th>
<td>&lt;/testsuite&gt;</td>
</tr><tr><th id="L238"><a href="#L238">238</a></th>
<td>&#34;&#34;&#34;)</td>
</tr><tr><th id="L239"><a href="#L239">239</a></th>
<td></td>
</tr><tr><th id="L240"><a href="#L240">240</a></th>
<td>&nbsp; &nbsp; def test_success(self):</td>
</tr><tr><th id="L241"><a href="#L241">241</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Regression test: Check whether a test run with a successful test</td>
</tr><tr><th id="L242"><a href="#L242">242</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; matches a previous run.&#34;&#34;&#34;</td>
</tr><tr><th id="L243"><a href="#L243">243</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L244"><a href="#L244">244</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L245"><a href="#L245">245</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pass</td>
</tr><tr><th id="L246"><a href="#L246">246</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._try_test_run(TestTest, &#34;&#34;&#34;&lt;testsuite errors=&#34;0&#34; failures=&#34;0&#34; name=&#34;unittest.TestSuite&#34; tests=&#34;1&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L247"><a href="#L247">247</a></th>
<td>&nbsp; &lt;testcase classname=&#34;__main__.TestTest&#34; name=&#34;test_foo&#34; time=&#34;0.000&#34;&gt;&lt;/testcase&gt;</td>
</tr><tr><th id="L248"><a href="#L248">248</a></th>
<td>&nbsp; &lt;system-out&gt;&lt;![CDATA[]]&gt;&lt;/system-out&gt;</td>
</tr><tr><th id="L249"><a href="#L249">249</a></th>
<td>&nbsp; &lt;system-err&gt;&lt;![CDATA[]]&gt;&lt;/system-err&gt;</td>
</tr><tr><th id="L250"><a href="#L250">250</a></th>
<td>&lt;/testsuite&gt;</td>
</tr><tr><th id="L251"><a href="#L251">251</a></th>
<td>&#34;&#34;&#34;)</td>
</tr><tr><th id="L252"><a href="#L252">252</a></th>
<td></td>
</tr><tr><th id="L253"><a href="#L253">253</a></th>
<td>&nbsp; &nbsp; def test_failure(self):</td>
</tr><tr><th id="L254"><a href="#L254">254</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Regression test: Check whether a test run with a failing test</td>
</tr><tr><th id="L255"><a href="#L255">255</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; matches a previous run.&#34;&#34;&#34;</td>
</tr><tr><th id="L256"><a href="#L256">256</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L257"><a href="#L257">257</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L258"><a href="#L258">258</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; self.assert_(False)</td>
</tr><tr><th id="L259"><a href="#L259">259</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._try_test_run(TestTest, &#34;&#34;&#34;&lt;testsuite errors=&#34;0&#34; failures=&#34;1&#34; name=&#34;unittest.TestSuite&#34; tests=&#34;1&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L260"><a href="#L260">260</a></th>
<td>&nbsp; &lt;testcase classname=&#34;__main__.TestTest&#34; name=&#34;test_foo&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L261"><a href="#L261">261</a></th>
<td>&nbsp; &nbsp; &lt;failure type=&#34;exceptions.AssertionError&#34;&gt;Foobar&lt;/failure&gt;</td>
</tr><tr><th id="L262"><a href="#L262">262</a></th>
<td>&nbsp; &lt;/testcase&gt;</td>
</tr><tr><th id="L263"><a href="#L263">263</a></th>
<td>&nbsp; &lt;system-out&gt;&lt;![CDATA[]]&gt;&lt;/system-out&gt;</td>
</tr><tr><th id="L264"><a href="#L264">264</a></th>
<td>&nbsp; &lt;system-err&gt;&lt;![CDATA[]]&gt;&lt;/system-err&gt;</td>
</tr><tr><th id="L265"><a href="#L265">265</a></th>
<td>&lt;/testsuite&gt;</td>
</tr><tr><th id="L266"><a href="#L266">266</a></th>
<td>&#34;&#34;&#34;)</td>
</tr><tr><th id="L267"><a href="#L267">267</a></th>
<td></td>
</tr><tr><th id="L268"><a href="#L268">268</a></th>
<td>&nbsp; &nbsp; def test_error(self):</td>
</tr><tr><th id="L269"><a href="#L269">269</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Regression test: Check whether a test run with a erroneous test</td>
</tr><tr><th id="L270"><a href="#L270">270</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; matches a previous run.&#34;&#34;&#34;</td>
</tr><tr><th id="L271"><a href="#L271">271</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L272"><a href="#L272">272</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L273"><a href="#L273">273</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; raise IndexError()</td>
</tr><tr><th id="L274"><a href="#L274">274</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._try_test_run(TestTest, &#34;&#34;&#34;&lt;testsuite errors=&#34;1&#34; failures=&#34;0&#34; name=&#34;unittest.TestSuite&#34; tests=&#34;1&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L275"><a href="#L275">275</a></th>
<td>&nbsp; &lt;testcase classname=&#34;__main__.TestTest&#34; name=&#34;test_foo&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L276"><a href="#L276">276</a></th>
<td>&nbsp; &nbsp; &lt;error type=&#34;exceptions.IndexError&#34;&gt;Foobar&lt;/error&gt;</td>
</tr><tr><th id="L277"><a href="#L277">277</a></th>
<td>&nbsp; &lt;/testcase&gt;</td>
</tr><tr><th id="L278"><a href="#L278">278</a></th>
<td>&nbsp; &lt;system-out&gt;&lt;![CDATA[]]&gt;&lt;/system-out&gt;</td>
</tr><tr><th id="L279"><a href="#L279">279</a></th>
<td>&nbsp; &lt;system-err&gt;&lt;![CDATA[]]&gt;&lt;/system-err&gt;</td>
</tr><tr><th id="L280"><a href="#L280">280</a></th>
<td>&lt;/testsuite&gt;</td>
</tr><tr><th id="L281"><a href="#L281">281</a></th>
<td>&#34;&#34;&#34;)</td>
</tr><tr><th id="L282"><a href="#L282">282</a></th>
<td></td>
</tr><tr><th id="L283"><a href="#L283">283</a></th>
<td>&nbsp; &nbsp; def test_stdout_capture(self):</td>
</tr><tr><th id="L284"><a href="#L284">284</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Regression test: Check whether a test run with output to stdout</td>
</tr><tr><th id="L285"><a href="#L285">285</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; matches a previous run.&#34;&#34;&#34;</td>
</tr><tr><th id="L286"><a href="#L286">286</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L287"><a href="#L287">287</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L288"><a href="#L288">288</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; print &#34;Test&#34;</td>
</tr><tr><th id="L289"><a href="#L289">289</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._try_test_run(TestTest, &#34;&#34;&#34;&lt;testsuite errors=&#34;0&#34; failures=&#34;0&#34; name=&#34;unittest.TestSuite&#34; tests=&#34;1&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L290"><a href="#L290">290</a></th>
<td>&nbsp; &lt;testcase classname=&#34;__main__.TestTest&#34; name=&#34;test_foo&#34; time=&#34;0.000&#34;&gt;&lt;/testcase&gt;</td>
</tr><tr><th id="L291"><a href="#L291">291</a></th>
<td>&nbsp; &lt;system-out&gt;&lt;![CDATA[Test</td>
</tr><tr><th id="L292"><a href="#L292">292</a></th>
<td>]]&gt;&lt;/system-out&gt;</td>
</tr><tr><th id="L293"><a href="#L293">293</a></th>
<td>&nbsp; &lt;system-err&gt;&lt;![CDATA[]]&gt;&lt;/system-err&gt;</td>
</tr><tr><th id="L294"><a href="#L294">294</a></th>
<td>&lt;/testsuite&gt;</td>
</tr><tr><th id="L295"><a href="#L295">295</a></th>
<td>&#34;&#34;&#34;)</td>
</tr><tr><th id="L296"><a href="#L296">296</a></th>
<td></td>
</tr><tr><th id="L297"><a href="#L297">297</a></th>
<td>&nbsp; &nbsp; def test_stderr_capture(self):</td>
</tr><tr><th id="L298"><a href="#L298">298</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Regression test: Check whether a test run with output to stderr</td>
</tr><tr><th id="L299"><a href="#L299">299</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; matches a previous run.&#34;&#34;&#34;</td>
</tr><tr><th id="L300"><a href="#L300">300</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L301"><a href="#L301">301</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L302"><a href="#L302">302</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; print &gt;&gt;sys.stderr, &#34;Test&#34;</td>
</tr><tr><th id="L303"><a href="#L303">303</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; self._try_test_run(TestTest, &#34;&#34;&#34;&lt;testsuite errors=&#34;0&#34; failures=&#34;0&#34; name=&#34;unittest.TestSuite&#34; tests=&#34;1&#34; time=&#34;0.000&#34;&gt;</td>
</tr><tr><th id="L304"><a href="#L304">304</a></th>
<td>&nbsp; &lt;testcase classname=&#34;__main__.TestTest&#34; name=&#34;test_foo&#34; time=&#34;0.000&#34;&gt;&lt;/testcase&gt;</td>
</tr><tr><th id="L305"><a href="#L305">305</a></th>
<td>&nbsp; &lt;system-out&gt;&lt;![CDATA[]]&gt;&lt;/system-out&gt;</td>
</tr><tr><th id="L306"><a href="#L306">306</a></th>
<td>&nbsp; &lt;system-err&gt;&lt;![CDATA[Test</td>
</tr><tr><th id="L307"><a href="#L307">307</a></th>
<td>]]&gt;&lt;/system-err&gt;</td>
</tr><tr><th id="L308"><a href="#L308">308</a></th>
<td>&lt;/testsuite&gt;</td>
</tr><tr><th id="L309"><a href="#L309">309</a></th>
<td>&#34;&#34;&#34;)</td>
</tr><tr><th id="L310"><a href="#L310">310</a></th>
<td></td>
</tr><tr><th id="L311"><a href="#L311">311</a></th>
<td>&nbsp; &nbsp; class NullStream(object):</td>
</tr><tr><th id="L312"><a href="#L312">312</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;A file-like object that discards everything written to it.&#34;&#34;&#34;</td>
</tr><tr><th id="L313"><a href="#L313">313</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; def write(self, buffer):</td>
</tr><tr><th id="L314"><a href="#L314">314</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pass</td>
</tr><tr><th id="L315"><a href="#L315">315</a></th>
<td></td>
</tr><tr><th id="L316"><a href="#L316">316</a></th>
<td>&nbsp; &nbsp; def test_unittests_changing_stdout(self):</td>
</tr><tr><th id="L317"><a href="#L317">317</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Check whether the XmlTestRunner recovers gracefully from unit tests</td>
</tr><tr><th id="L318"><a href="#L318">318</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; that change stdout, but don't change it back properly.</td>
</tr><tr><th id="L319"><a href="#L319">319</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L320"><a href="#L320">320</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L321"><a href="#L321">321</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L322"><a href="#L322">322</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sys.stdout = XmlTestRunnerTest.NullStream()</td>
</tr><tr><th id="L323"><a href="#L323">323</a></th>
<td></td>
</tr><tr><th id="L324"><a href="#L324">324</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner = XmlTestRunner(self._stream)</td>
</tr><tr><th id="L325"><a href="#L325">325</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner.run(unittest.makeSuite(TestTest))</td>
</tr><tr><th id="L326"><a href="#L326">326</a></th>
<td></td>
</tr><tr><th id="L327"><a href="#L327">327</a></th>
<td>&nbsp; &nbsp; def test_unittests_changing_stderr(self):</td>
</tr><tr><th id="L328"><a href="#L328">328</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;Check whether the XmlTestRunner recovers gracefully from unit tests</td>
</tr><tr><th id="L329"><a href="#L329">329</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; that change stderr, but don't change it back properly.</td>
</tr><tr><th id="L330"><a href="#L330">330</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &#34;&#34;&#34;</td>
</tr><tr><th id="L331"><a href="#L331">331</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; class TestTest(unittest.TestCase):</td>
</tr><tr><th id="L332"><a href="#L332">332</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def test_foo(self):</td>
</tr><tr><th id="L333"><a href="#L333">333</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sys.stderr = XmlTestRunnerTest.NullStream()</td>
</tr><tr><th id="L334"><a href="#L334">334</a></th>
<td></td>
</tr><tr><th id="L335"><a href="#L335">335</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner = XmlTestRunner(self._stream)</td>
</tr><tr><th id="L336"><a href="#L336">336</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner.run(unittest.makeSuite(TestTest))</td>
</tr><tr><th id="L337"><a href="#L337">337</a></th>
<td></td>
</tr><tr><th id="L338"><a href="#L338">338</a></th>
<td></td>
</tr><tr><th id="L339"><a href="#L339">339</a></th>
<td>if __name__ == &#34;__main__&#34;:</td>
</tr><tr><th id="L340"><a href="#L340">340</a></th>
<td>&nbsp; &nbsp; suite = unittest.makeSuite(XmlTestRunnerTest)</td>
</tr><tr><th id="L341"><a href="#L341">341</a></th>
<td>&nbsp; &nbsp; unittest.TextTestRunner().run(suite)</td>
</tr></tbody></table>
  </div>

 <div id="help">
  <strong>Note:</strong> See <a href="/wiki/TracBrowser">TracBrowser</a> for help on using the browser.
 </div>

  <div id="anydiff">
   <form action="/anydiff" method="get">
    <div class="buttons">
     <input type="hidden" name="new_path" value="/TV.com/trunk/src/python-test/xmlrunner.py" />
     <input type="hidden" name="old_path" value="/TV.com/trunk/src/python-test/xmlrunner.py" />
     <input type="hidden" name="new_rev" value="" />
     <input type="hidden" name="old_rev" value="" />
     <input type="submit" value="View changes..." title="Prepare an Arbitrary Diff" />
    </div>
   </form>
  </div>

</div>
</div>
<script type="text/javascript">searchHighlight()</script>
<div id="altlinks"><h3>Download in other formats:</h3><ul><li class="first"><a href="/browser/TV.com/trunk/src/python-test/xmlrunner.py?format=txt">Plain Text</a></li><li class="last"><a href="/browser/TV.com/trunk/src/python-test/xmlrunner.py?format=raw">Original Format</a></li></ul></div>

</div>

<div id="footer">
 <hr />
 <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/trac/trac_logo_mini.png" height="30" width="107"
   alt="Trac Powered"/></a>
 <p class="left">
  Powered by <a href="/about"><strong>Trac 0.10.3</strong></a><br />
  By <a href="http://www.edgewall.org/">Edgewall Software</a>.
 </p>
 <p class="right">
  Visit the Trac open source project at<br /><a href="http://trac.edgewall.com/">http://trac.edgewall.com/</a><script type="text/javascript"></script>
 </p>
</div>



 </body>
</html>

