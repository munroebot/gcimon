<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
 <title>/TV.com/trunk/src/python-test/alltestsuite.py - XBMC - Trac</title><link rel="start" href="/wiki" /><link rel="search" href="/search" /><link rel="help" href="/wiki/TracGuide" /><link rel="stylesheet" href="/trac/css/trac.css" type="text/css" /><link rel="stylesheet" href="/trac/css/code.css" type="text/css" /><link rel="stylesheet" href="/trac/css/browser.css" type="text/css" /><link rel="icon" href="/chrome/common/trac.ico" type="image/x-icon" /><link rel="shortcut icon" href="/chrome/common/trac.ico" type="image/x-icon" /><link rel="up" href="/browser/TV.com/trunk/src/python-test" title="Parent directory" /><link rel="alternate" href="/browser/TV.com/trunk/src/python-test/alltestsuite.py?format=txt" title="Plain Text" type="text/plain" /><link rel="alternate" href="/browser/TV.com/trunk/src/python-test/alltestsuite.py?format=raw" title="Original Format" type="text/x-python; charset=iso-8859-15" /><style type="text/css">
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
  <li class="first"><a href="/changeset/295/TV.com/trunk/src/python-test/alltestsuite.py">
   Last Change</a></li>
  <li class="last"><a href="/log/TV.com/trunk/src/python-test/alltestsuite.py">
   Revision Log</a></li>
 </ul>
</div>


<div id="searchable">
<div id="content" class="browser">
 <h1><a class="first" title="Go to root directory" href="/browser">root</a><span class="sep">/</span><a title="View TV.com" href="/browser/TV.com">TV.com</a><span class="sep">/</span><a title="View trunk" href="/browser/TV.com/trunk">trunk</a><span class="sep">/</span><a title="View src" href="/browser/TV.com/trunk/src">src</a><span class="sep">/</span><a title="View python-test" href="/browser/TV.com/trunk/src/python-test">python-test</a><span class="sep">/</span><a title="View alltestsuite.py" href="/browser/TV.com/trunk/src/python-test/alltestsuite.py">alltestsuite.py</a></h1>

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
     Revision <a href="/changeset/295">295</a>, 2.1 kB
     (checked in by redsolo, 9 months ago)
    </th></tr><tr>
    <td class="message"><p>
Fixed XML report <br />
</p>
</td>
   </tr>
  </table>
  <div id="preview"><table class="code"><thead><tr><th class="lineno">Line</th><th class="content">&nbsp;</th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th>
<td>'''</td>
</tr><tr><th id="L2"><a href="#L2">2</a></th>
<td>GNU General Public License.</td>
</tr><tr><th id="L3"><a href="#L3">3</a></th>
<td>'XBMC TV.COM script' is free software; you can redistribute it and/or modify</td>
</tr><tr><th id="L4"><a href="#L4">4</a></th>
<td>it under the terms of the GNU General Public License as published by</td>
</tr><tr><th id="L5"><a href="#L5">5</a></th>
<td>the Free Software Foundation; either version 2 of the License, or</td>
</tr><tr><th id="L6"><a href="#L6">6</a></th>
<td>(at your option) any later version.</td>
</tr><tr><th id="L7"><a href="#L7">7</a></th>
<td></td>
</tr><tr><th id="L8"><a href="#L8">8</a></th>
<td>'XBMC TV.COM script' is distributed in the hope that it will be useful,</td>
</tr><tr><th id="L9"><a href="#L9">9</a></th>
<td>but WITHOUT ANY WARRANTY; without even the implied warranty of</td>
</tr><tr><th id="L10"><a href="#L10">10</a></th>
<td>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.&nbsp; See the</td>
</tr><tr><th id="L11"><a href="#L11">11</a></th>
<td>GNU General Public License for more details.</td>
</tr><tr><th id="L12"><a href="#L12">12</a></th>
<td></td>
</tr><tr><th id="L13"><a href="#L13">13</a></th>
<td>You should have received a copy of the GNU General Public License</td>
</tr><tr><th id="L14"><a href="#L14">14</a></th>
<td>along with 'XBMC TV.COM script'; if not, write to the Free Software</td>
</tr><tr><th id="L15"><a href="#L15">15</a></th>
<td>Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA&nbsp; 02110-1301&nbsp; USA</td>
</tr><tr><th id="L16"><a href="#L16">16</a></th>
<td>'''</td>
</tr><tr><th id="L17"><a href="#L17">17</a></th>
<td>from searchshowtestcase import SearchShowTestCase</td>
</tr><tr><th id="L18"><a href="#L18">18</a></th>
<td>from searchpersontestcase import SearchPersonTestCase</td>
</tr><tr><th id="L19"><a href="#L19">19</a></th>
<td>from showtestcase import ShowTestCase</td>
</tr><tr><th id="L20"><a href="#L20">20</a></th>
<td>from videotestcase import VideoTestCase</td>
</tr><tr><th id="L21"><a href="#L21">21</a></th>
<td>from episodetestcase import EpisodeTestCase</td>
</tr><tr><th id="L22"><a href="#L22">22</a></th>
<td>from persontestcase import PersonTestCase</td>
</tr><tr><th id="L23"><a href="#L23">23</a></th>
<td>from tvguicontrollertestcase import TvGuiControllerTestCase</td>
</tr><tr><th id="L24"><a href="#L24">24</a></th>
<td>from actionhistorytestcase import ActionHistoryTestCase</td>
</tr><tr><th id="L25"><a href="#L25">25</a></th>
<td>from actiontestcase import ActionTestCase</td>
</tr><tr><th id="L26"><a href="#L26">26</a></th>
<td></td>
</tr><tr><th id="L27"><a href="#L27">27</a></th>
<td>import unittest</td>
</tr><tr><th id="L28"><a href="#L28">28</a></th>
<td>import HTMLTestRunner</td>
</tr><tr><th id="L29"><a href="#L29">29</a></th>
<td>import sys</td>
</tr><tr><th id="L30"><a href="#L30">30</a></th>
<td>import xmlrunner</td>
</tr><tr><th id="L31"><a href="#L31">31</a></th>
<td></td>
</tr><tr><th id="L32"><a href="#L32">32</a></th>
<td>suite = unittest.TestSuite([</td>
</tr><tr><th id="L33"><a href="#L33">33</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(ShowTestCase),</td>
</tr><tr><th id="L34"><a href="#L34">34</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(EpisodeTestCase),</td>
</tr><tr><th id="L35"><a href="#L35">35</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(VideoTestCase),</td>
</tr><tr><th id="L36"><a href="#L36">36</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(SearchShowTestCase),</td>
</tr><tr><th id="L37"><a href="#L37">37</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(SearchPersonTestCase),</td>
</tr><tr><th id="L38"><a href="#L38">38</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(PersonTestCase),</td>
</tr><tr><th id="L39"><a href="#L39">39</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(TvGuiControllerTestCase),</td>
</tr><tr><th id="L40"><a href="#L40">40</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(ActionTestCase),</td>
</tr><tr><th id="L41"><a href="#L41">41</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unittest.TestLoader().loadTestsFromTestCase(ActionHistoryTestCase)</td>
</tr><tr><th id="L42"><a href="#L42">42</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; ])</td>
</tr><tr><th id="L43"><a href="#L43">43</a></th>
<td></td>
</tr><tr><th id="L44"><a href="#L44">44</a></th>
<td>if __name__ == '__main__': </td>
</tr><tr><th id="L45"><a href="#L45">45</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner = unittest.TextTestRunner()</td>
</tr><tr><th id="L46"><a href="#L46">46</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; for argstr in sys.argv:</td>
</tr><tr><th id="L47"><a href="#L47">47</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if (argstr == &#34;html&#34;):</td>
</tr><tr><th id="L48"><a href="#L48">48</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; runner = HTMLTestRunner.HTMLTestRunner(verbosity=0)</td>
</tr><tr><th id="L49"><a href="#L49">49</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if (argstr == &#34;xml&#34;):</td>
</tr><tr><th id="L50"><a href="#L50">50</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; runner = xmlrunner.XmlTestRunner(sys.stdout)</td>
</tr><tr><th id="L51"><a href="#L51">51</a></th>
<td>&nbsp; &nbsp; &nbsp; &nbsp; runner.run(suite)</td>
</tr></tbody></table>
  </div>

 <div id="help">
  <strong>Note:</strong> See <a href="/wiki/TracBrowser">TracBrowser</a> for help on using the browser.
 </div>

  <div id="anydiff">
   <form action="/anydiff" method="get">
    <div class="buttons">
     <input type="hidden" name="new_path" value="/TV.com/trunk/src/python-test/alltestsuite.py" />
     <input type="hidden" name="old_path" value="/TV.com/trunk/src/python-test/alltestsuite.py" />
     <input type="hidden" name="new_rev" value="" />
     <input type="hidden" name="old_rev" value="" />
     <input type="submit" value="View changes..." title="Prepare an Arbitrary Diff" />
    </div>
   </form>
  </div>

</div>
</div>
<script type="text/javascript">searchHighlight()</script>
<div id="altlinks"><h3>Download in other formats:</h3><ul><li class="first"><a href="/browser/TV.com/trunk/src/python-test/alltestsuite.py?format=txt">Plain Text</a></li><li class="last"><a href="/browser/TV.com/trunk/src/python-test/alltestsuite.py?format=raw">Original Format</a></li></ul></div>

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

