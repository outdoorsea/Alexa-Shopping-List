Python Package for controlling Alexa devices (echo dot, etc)
programmatically. This was originally designed for
[alexa_media_player](https://github.com/custom-components/alexa_media_player){.reference
.external} a custom_component for [Home
Assistant](https://www.home-assistant.io/){.reference .external}.

**NOTE:** Alexa has no official API; therefore, this library may stop
working at any time without warning.


 {#credits .section}
# Credits[¶](#credits "Permalink to this headline"){.headerlink}

Originally inspired by [this
blog](https://blog.loetzimmer.de/2017/10/amazon-alexa-hort-auf-die-shell-echo.html){.reference
.external}
[(GitHub)](https://github.com/thorsten-gehrig/alexa-remote-control){.reference
.external}. Additional scaffolding from
[simplisafe-python](https://github.com/bachya/simplisafe-python){.reference
.external}


 {#contributing .section}
# Contributing[¶](#contributing "Permalink to this headline"){.headerlink}

1.  [Check for open
    features/bugs](https://gitlab.com/keatontaylor/alexapy/issues){.reference
    .external} or [initiate a discussion on
    one](https://gitlab.com/keatontaylor/alexapy/issues/new){.reference
    .external}.

2.  [Fork the
    repository](https://gitlab.com/keatontaylor/alexapy/forks/new){.reference
    .external}.

3.  Install the dev environment: [`make`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`init`{.docutils .literal .notranslate}]{.pre}.

4.  Enter the virtual environment: [`pipenv`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`shell`{.docutils .literal .notranslate}]{.pre}

5.  Code your new feature or bug fix.

6.  Write a test that covers your new functionality.

7.  Update [`README.md`{.docutils .literal .notranslate}]{.pre} with any
    new documentation.

8.  Run tests and ensure 100% code coverage for your contribution:
    [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils
    .literal .notranslate}[`coverage`{.docutils .literal
    .notranslate}]{.pre}

9.  Ensure you have no linting errors: [`make`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`lint`{.docutils .literal .notranslate}]{.pre}

10. Ensure you have typed your code correctly: [`make`{.docutils
    .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`typing`{.docutils .literal .notranslate}]{.pre}

11. Add yourself to [`AUTHORS.md`{.docutils .literal
    .notranslate}]{.pre}.

12. Submit a pull request!


 {#license .section}
# License[¶](#license "Permalink to this headline"){.headerlink}

[Apache-2.0](LICENSE){.reference .external}. By providing a
contribution, you agree the contribution is licensed under Apache-2.0.


 {#api-reference .section}
# API Reference[¶](#api-reference "Permalink to this headline"){.headerlink}

[See the docs
📚](https://alexapy.readthedocs.io/en/latest/index.html){.reference
.external}.


 {#id1 .section}
# API Reference[¶](#id1 "Permalink to this headline"){.headerlink}

:: {.toctree-wrapper .compound}
[]{#document-alexapy/alexapy}

: {#module-alexapy .section}
[]{#alexapy}

## [`alexapy`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}

 {#contents .contents .local .topic}
- [Submodules](#submodules){#id3 .reference .internal}

- [Functions](#functions){#id4 .reference .internal}

- [Classes](#classes){#id5 .reference .internal}

- [Exceptions](#exceptions){#id6 .reference .internal}


:: {#submodules .section}
### [Submodules](#id3){.toc-backref}[¶](#submodules "Permalink to this headline"){.headerlink}

: {.toctree-wrapper .compound}
[]{#document-alexapy/alexapy.aiohttp}[]{#document-alexapy/alexapy.alexaapi}

 {#module-alexapy.alexaapi .section}
[]{#alexapy-alexaapi}

#### [`alexapy.alexaapi`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.alexaapi "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

API access.

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}


[]{#document-alexapy/alexapy.alexalogin}

 {#module-alexapy.alexalogin .section}
[]{#alexapy-alexalogin}

#### [`alexapy.alexalogin`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.alexalogin "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

Login class.

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}


[]{#document-alexapy/alexapy.alexaproxy}

 {#module-alexapy.alexaproxy .section}
[]{#alexapy-alexaproxy}

#### [`alexapy.alexaproxy`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.alexaproxy "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

This provides a login by proxy method. Built on
[https://github.com/alandtse/auth_capture_proxy](https://github.com/alandtse/auth_capture_proxy){.reference
.external}

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}


[]{#document-alexapy/alexapy.alexawebsocket}

 {#module-alexapy.alexawebsocket .section}
[]{#alexapy-alexawebsocket}

#### [`alexapy.alexawebsocket`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.alexawebsocket "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

Websocket library.

This library is based on MIT code from
[https://github.com/Apollon77/alexa-remote](https://github.com/Apollon77/alexa-remote){.reference
.external}.

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}


[]{#document-alexapy/alexapy.const}

 {#module-alexapy.const .section}
[]{#alexapy-const}

#### [`alexapy.const`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.const "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

Constants.

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}


[]{#document-alexapy/alexapy.errors}

 {#module-alexapy.errors .section}
[]{#alexapy-errors}

#### [`alexapy.errors`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.errors "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

Package errors.

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}


[]{#document-alexapy/alexapy.helpers}

 {#module-alexapy.helpers .section}
[]{#alexapy-helpers}

#### [`alexapy.helpers`{.docutils .literal .notranslate}]{.pre}[¶](#module-alexapy.helpers "Permalink to this headline"){.headerlink}

Python Package for controlling Alexa devices (echo dot, etc)
programmatically.

SPDX-License-Identifier: Apache-2.0

Helpers.

For more details about this api, please refer to the documentation at
[https://gitlab.com/keatontaylor/alexapy](https://gitlab.com/keatontaylor/alexapy){.reference
.external}

:
::

 {#functions .section}
### [Functions](#id4){.toc-backref}[¶](#functions "Permalink to this headline"){.headerlink}

- [[`hide_email()`{.xref .py .py-func .docutils .literal
  .notranslate}]{.pre}](#alexapy.hide_email "alexapy.hide_email"){.reference
  .internal}: Obfuscate email.

- [[`hide_serial()`{.xref .py .py-func .docutils .literal
  .notranslate}]{.pre}](#alexapy.hide_serial "alexapy.hide_serial"){.reference
  .internal}: Obfuscate serial.

- [[`obfuscate()`{.xref .py .py-func .docutils .literal
  .notranslate}]{.pre}](#alexapy.obfuscate "alexapy.obfuscate"){.reference
  .internal}: Obfuscate email, password, and other known sensitive keys.

[[alexapy.]{.pre}]{.sig-prename .descclassname}[[hide_email]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[email]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[str]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.hide_email "Permalink to this definition"){.headerlink}

:   Obfuscate email.

<!-- -->

[[alexapy.]{.pre}]{.sig-prename .descclassname}[[hide_serial]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[item]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Union]{.pre}[[\[]{.pre}]{.p}[dict]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[list]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Union]{.pre}[[\[]{.pre}]{.p}[dict]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[list]{.pre}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.hide_serial "Permalink to this definition"){.headerlink}

:   Obfuscate serial.

<!-- -->

[[alexapy.]{.pre}]{.sig-prename .descclassname}[[obfuscate]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[item]{.pre}]{.n}*[)]{.sig-paren}[¶](#alexapy.obfuscate "Permalink to this definition"){.headerlink}

:   Obfuscate email, password, and other known sensitive keys.


 {#classes .section}
### [Classes](#id5){.toc-backref}[¶](#classes "Permalink to this headline"){.headerlink}

- [[`AlexaLogin`{.xref .py .py-class .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexaLogin "alexapy.AlexaLogin"){.reference
  .internal}: Class to handle login connection to Alexa. This class will
  not reconnect.

- [[`AlexaAPI`{.xref .py .py-class .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexaAPI "alexapy.AlexaAPI"){.reference
  .internal}: Class for accessing a specific Alexa device using rest
  API.

- [[`AlexaProxy`{.xref .py .py-class .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexaProxy "alexapy.AlexaProxy"){.reference
  .internal}: Class to handle proxy login connections to Alexa.

- [[`WebsocketEchoClient`{.xref .py .py-class .docutils .literal
  .notranslate}]{.pre}](#alexapy.WebsocketEchoClient "alexapy.WebsocketEchoClient"){.reference
  .internal}: WebSocket Client Class for Echo Devices.

*[class]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexaLogin]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[url]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[email]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[password]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[outputpath]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}]{.n}*, *[[debug]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[False]{.pre}]{.default_value}*, *[[otp_secret]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'\']{.pre}]{.default_value}*, *[[oauth]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[uuid]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[oauth_login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#alexapy.AlexaLogin "Permalink to this definition"){.headerlink}

:   Class to handle login connection to Alexa. This class will not
    reconnect.

    Args: url (string): Localized Amazon domain (e.g., amazon.com) email
    (string): Amazon login account password (string): Password for
    Amazon login account outputpath (function): Local path with write
    access for storing files debug (boolean): Enable additional
    debugging including debug file creation otp_secret (string): TOTP
    Secret key for automatic 2FA filling uuid: (string): Unique 32 char
    hex to serve as app serial number for registration

    Inheritance

     graphviz
    Inheritance diagram of AlexaLogin


    *[async]{.pre}[ ]{.w}*[[check_domain]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.check_domain "Permalink to this definition"){.headerlink}

    :   Check whether logged into appropriate login domain.

        Returns

        :   bool: True if in correct domain

    *[async]{.pre}[ ]{.w}*[[close]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.close "Permalink to this definition"){.headerlink}

    :   Close connection for login.

    *[property]{.pre}[ ]{.w}*[[close_requested]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[bool]{.pre}*[¶](#alexapy.AlexaLogin.close_requested "Permalink to this definition"){.headerlink}

    :   Return whether this Login has been asked to close.

    *[property]{.pre}[ ]{.w}*[[customer_id]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}*[¶](#alexapy.AlexaLogin.customer_id "Permalink to this definition"){.headerlink}

    :   Return customer_id for this Login.

    *[property]{.pre}[ ]{.w}*[[email]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[str]{.pre}*[¶](#alexapy.AlexaLogin.email "Permalink to this definition"){.headerlink}

    :   Return email or mobile account for this Login.

    *[async]{.pre}[ ]{.w}*[[exchange_token_for_cookies]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.exchange_token_for_cookies "Permalink to this definition"){.headerlink}

    :   Generate new session cookies using refresh token.

        Returns

        :   bool: True if succesful

    *[async]{.pre}[ ]{.w}*[[finalize_login]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.finalize_login "Permalink to this definition"){.headerlink}

    :   Perform final steps after successful login.

    *[async]{.pre}[ ]{.w}*[[get_csrf]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.get_csrf "Permalink to this definition"){.headerlink}

    :   Generate csrf if missing.

        Returns

        :   bool: True if csrf is found

    *[classmethod]{.pre}[ ]{.w}*[[get_inputs]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[soup]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bs4.BeautifulSoup]{.pre}]{.n}*, *[[searchfield]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.get_inputs "Permalink to this definition"){.headerlink}

    :   Parse soup for form with searchfield.

    *[async]{.pre}[ ]{.w}*[[get_tokens]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.get_tokens "Permalink to this definition"){.headerlink}

    :   Get access and refresh tokens after registering device using
        cookies.

        Returns

        :   True if successful.

        Return type

        :   bool

    [[get_totp_token]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[str]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.get_totp_token "Permalink to this definition"){.headerlink}

    :   Generate Timed based OTP token.

        Returns

        :   Text: OTP for current time.

    *[property]{.pre}[ ]{.w}*[[lastreq]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[Optional]{.pre}[[\[]{.pre}]{.p}[[alexapy.aiohttp.client_reqrep.ClientResponse]{.pre}](index.html#alexapy.aiohttp.client_reqrep.ClientResponse "alexapy.aiohttp.client_reqrep.ClientResponse"){.reference .internal}[[\]]{.pre}]{.p}*[¶](#alexapy.AlexaLogin.lastreq "Permalink to this definition"){.headerlink}

    :   Return last response for last request for this Login.

    *[property]{.pre}[ ]{.w}*[[links]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[str]{.pre}*[¶](#alexapy.AlexaLogin.links "Permalink to this definition"){.headerlink}

    :   Return string list of links from last page for this Login.

    *[async]{.pre}[ ]{.w}*[[load_cookie]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cookies_txt]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'\']{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.load_cookie "Permalink to this definition"){.headerlink}

    :   Load cookie from disk.

    *[async]{.pre}[ ]{.w}*[[login]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cookies]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[data]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.login "Permalink to this definition"){.headerlink}

    :   Login to Amazon.

    *[property]{.pre}[ ]{.w}*[[password]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[str]{.pre}*[¶](#alexapy.AlexaLogin.password "Permalink to this definition"){.headerlink}

    :   Return password for this Login.

    *[async]{.pre}[ ]{.w}*[[refresh_access_token]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.refresh_access_token "Permalink to this definition"){.headerlink}

    :   Refresh access token and expires in using refresh token.

        Returns

        :   bool: Return true if successful.

    *[async]{.pre}[ ]{.w}*[[reset]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.reset "Permalink to this definition"){.headerlink}

    :   Remove data related to existing login.

    *[async]{.pre}[ ]{.w}*[[save_cookiefile]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.save_cookiefile "Permalink to this definition"){.headerlink}

    :   Save login session cookies to file.

    *[property]{.pre}[ ]{.w}*[[session]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[Optional]{.pre}[[\[]{.pre}]{.p}[[alexapy.aiohttp.client.ClientSession]{.pre}](index.html#alexapy.aiohttp.client.ClientSession "alexapy.aiohttp.client.ClientSession"){.reference .internal}[[\]]{.pre}]{.p}*[¶](#alexapy.AlexaLogin.session "Permalink to this definition"){.headerlink}

    :   Return session for this Login.

    [[set_totp]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[otp_secret]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[pyotp.totp.TOTP]{.pre}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.set_totp "Permalink to this definition"){.headerlink}

    :   Enable a TOTP generator for the login.

        Args

        :   otp_secret (Text): Secret. If blank, it will remove the TOTP
            entry.

        Returns

        :   Optional\[pyotp.TOTP\]: The pyotp TOTP object

    *[property]{.pre}[ ]{.w}*[[start_url]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[yarl.URL]{.pre}*[¶](#alexapy.AlexaLogin.start_url "Permalink to this definition"){.headerlink}

    :   Return start url for this Login.

    *[async]{.pre}[ ]{.w}*[[test_loggedin]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cookies]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaLogin.test_loggedin "Permalink to this definition"){.headerlink}

    :   Function that will test the connection is logged in.

        Tests: - Attempts to get authenticaton and compares to expected
        login email Returns false if unsuccesful getting json or the
        emails don't match Returns false if no csrf found; necessary to
        issue commands

    *[property]{.pre}[ ]{.w}*[[url]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[str]{.pre}*[¶](#alexapy.AlexaLogin.url "Permalink to this definition"){.headerlink}

    :   Return url for this Login.

<!-- -->

*[class]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexaAPI]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[device]{.pre}]{.n}*, *[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren}[¶](#alexapy.AlexaAPI "Permalink to this definition"){.headerlink}

:   Class for accessing a specific Alexa device using rest API.

    Args: device (AlexaClient): Instance of an AlexaClient to access
    login (AlexaLogin): Successfully logged in AlexaLogin

    Inheritance

     graphviz
    Inheritance diagram of AlexaAPI


    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[clear_history]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[items]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[int]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[50]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.clear_history "Permalink to this definition"){.headerlink}

    :   Clear entries in history.

    *[async]{.pre}[ ]{.w}*[[disconnect_bluetooth]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.disconnect_bluetooth "Permalink to this definition"){.headerlink}

    :   Disconnect all bluetooth devices.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[force_logout]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.force_logout "Permalink to this definition"){.headerlink}

    :   Force logout.

        Raises

        :   AlexapyLoginError: Raise AlexapyLoginError

    *[async]{.pre}[ ]{.w}*[[forward]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.forward "Permalink to this definition"){.headerlink}

    :   Fastforward.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_activities]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[items]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[int]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[10]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_activities "Permalink to this definition"){.headerlink}

    :   Get activities json.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_authentication]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_authentication "Permalink to this definition"){.headerlink}

    :   Get authentication json.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_automations]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[items]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[int]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1000]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_automations "Permalink to this definition"){.headerlink}

    :   Identify all Alexa automations.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_bluetooth]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_bluetooth "Permalink to this definition"){.headerlink}

    :   Get paired bluetooth devices.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_device_preferences]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_device_preferences "Permalink to this definition"){.headerlink}

    :   Identify all Alexa device preferences.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_devices]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_devices "Permalink to this definition"){.headerlink}

    :   Identify all Alexa devices.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_dnd_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_dnd_state "Permalink to this definition"){.headerlink}

    :   Get Alexa DND states.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin

        Returns json

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_entity_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[entity_ids]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[List]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[appliance_ids]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[List]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_entity_state "Permalink to this definition"){.headerlink}

    :   Get the current state of multiple appliances.

        Note that this can take both entity_ids and appliance_ids. If
        you have both pieces of data available, prefer the entity id. A
        single entity might have multiple appliance ids. Its easier to
        ensure you don't miss data by just providing entity id instead.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin
        entity_ids (List\[Text\]): The list of entities you want
        information about. appliance_ids: (List\[Text\]): The list of
        appliances you want information about.

        Returns json

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_guard_details]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_guard_details "Permalink to this definition"){.headerlink}

    :   Get Alexa Guard details.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin

        Returns json

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_guard_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[entity_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_guard_state "Permalink to this definition"){.headerlink}

    :   Get state of Alexa guard.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin
        entity_id (Text): applianceId of RedRock Panel

        Returns json

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_last_device_serial]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[items]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[int]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[10]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_last_device_serial "Permalink to this definition"){.headerlink}

    :   Identify the last device's serial number and last summary.

        This will search the \[last items\] activity records and find
        the latest entry where Echo successfully responded.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_network_details]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_network_details "Permalink to this definition"){.headerlink}

    :   Get the network of devices that Alexa is aware of. This is the
        same as calling get_guard_details().

        Args: login: (AlexaLogin): Successfully logged in AlexaLogin

        Returns json

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[get_notifications]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_notifications "Permalink to this definition"){.headerlink}

    :   Get Alexa notifications.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin

        Returns json

    *[async]{.pre}[ ]{.w}*[[get_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.get_state "Permalink to this definition"){.headerlink}

    :   Get playing state.

    *[async]{.pre}[ ]{.w}*[[next]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.next "Permalink to this definition"){.headerlink}

    :   Play next.

    *[async]{.pre}[ ]{.w}*[[pause]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.pause "Permalink to this definition"){.headerlink}

    :   Pause.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[ping]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.ping "Permalink to this definition"){.headerlink}

    :   Ping.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin

        Returns json

    *[async]{.pre}[ ]{.w}*[[play]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.play "Permalink to this definition"){.headerlink}

    :   Play.

    *[async]{.pre}[ ]{.w}*[[play_music]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[provider_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[search_phrase]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[timer]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[int]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.play_music "Permalink to this definition"){.headerlink}

    :   Play music based on search.

        Parameters

        :   - **provider_id** (*Text*) -- Amazon music provider.

            - **search_phrase** (*Text*) -- Phrase to be searched for

            - **customer_id** (*Optional\[Text\],* *optional*) --
              CustomerId to use for authorization. When none specified
              this defaults to the logged in user. Used with households
              where others may have their own music.

            - **timer** (*Optional\[int\]*) -- Number of seconds to play
              before stopping.

            - **queue_delay** (*float,* *optional*) -- The number of
              seconds to wait for commands to queue together. Must be
              positive. Defaults to 1.5.

            - **extra** (*Dict*) -- Extra dictionary array;
              functionality undetermined

    *[async]{.pre}[ ]{.w}*[[play_sound]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[sound_string_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.play_sound "Permalink to this definition"){.headerlink}

    :   Play Alexa sound.

    *[async]{.pre}[ ]{.w}*[[previous]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.previous "Permalink to this definition"){.headerlink}

    :   Play previous.

    [[process_targets]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[targets]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[List]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[List]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.process_targets "Permalink to this definition"){.headerlink}

    :   Process targets list to generate list of devices.

        Keyword Arguments

        :

            targets {Optional\[List\[Text\]\]} -- List of serial numbers

            :   (default: {\[\]})

        Returns

        :   List\[Dict\[Text, Text\] -- List of device dicts

    *[async]{.pre}[ ]{.w}*[[repeat]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[setting]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.repeat "Permalink to this definition"){.headerlink}

    :   Repeat.

        setting (string) : true or false

    *[async]{.pre}[ ]{.w}*[[rewind]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.rewind "Permalink to this definition"){.headerlink}

    :   Rewind.

    *[async]{.pre}[ ]{.w}*[[run_behavior]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[node_data]{.pre}]{.n}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.run_behavior "Permalink to this definition"){.headerlink}

    :   Queue node_data for running a behavior in sequence.

        Amazon sequences and routines are based on node_data.

        Parameters

        :   - **node_data** (*dict,* *list of dicts*) -- The node_data
              to run.

            - **queue_delay** (*float,* *optional*) -- The number of
              seconds to wait for commands to queue together. Defaults
              to 1.5. Must be positive.

    *[async]{.pre}[ ]{.w}*[[run_custom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[text]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.run_custom "Permalink to this definition"){.headerlink}

    :   Run Alexa skill.

        This allows running exactly what you can say to alexa.

        Parameters

        :   - **text** (*string*) -- The full text you want alexa to
              execute.

            - **customer_id** (*string*) -- CustomerId to use for
              authorization. When none specified this defaults to the
              logged in user. Used with households where others may have
              their own music.

            - **queue_delay** (*float,* *optional*) -- The number of
              seconds to wait for commands to queue together. Defaults
              to 1.5. Must be positive.

            - **extra** (*Dict*) -- Extra dictionary array;
              functionality undetermined

    *[async]{.pre}[ ]{.w}*[[run_routine]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[utterance]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.run_routine "Permalink to this definition"){.headerlink}

    :   Run Alexa automation routine.

        This allows running of defined Alexa automation routines.

        Parameters

        :   - **utterance** (*string*) -- The Alexa utterance to run the
              routine.

            - **customer_id** (*string*) -- CustomerId to use for
              authorization. When none specified this defaults to the
              logged in user. Used with households where others may have
              their own music.

            - **queue_delay** (*float,* *optional*) -- The number of
              seconds to wait for commands to queue together. Defaults
              to 1.5. Must be positive.

    *[async]{.pre}[ ]{.w}*[[run_skill]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[skill_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.run_skill "Permalink to this definition"){.headerlink}

    :   Run Alexa skill.

        This allows running of defined Alexa skill.

        Parameters

        :   - **skill_id** (*string*) -- The full skill id.

            - **customer_id** (*string*) -- CustomerId to use for
              authorization. When none specified this defaults to the
              logged in user. Used with households where others may have
              their own music.

            - **queue_delay** (*float,* *optional*) -- The number of
              seconds to wait for commands to queue together. Defaults
              to 1.5. Must be positive.

    *[async]{.pre}[ ]{.w}*[[send_announcement]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[method]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'all\']{.pre}]{.default_value}*, *[[title]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'Announcement\']{.pre}]{.default_value}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[targets]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[List]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.send_announcement "Permalink to this definition"){.headerlink}

    :   Send announcment to Alexa devices.

        This uses the AlexaAnnouncement and allows visual display on the
        Show. It will beep prior to speaking.

        Args: message (string): The message to speak or display. method
        (string): speak, show, or all title (string): title to display
        on Echo show customer_id (string): CustomerId to use for
        authorization. When none

        > <div>
        >
        > specified this defaults to the logged in user. Used with
        > households where others may have their own music.
        >
        > </div>

        targets (list(string)): List of serialNumber or accountName to send the

        :   announcement to. Only those in this AlexaAPI account will be
            searched. If None, announce will be self.

        queue_delay (float, optional): The number of seconds to wait

        :   for commands to queue together. Defaults to 1.5. Must be
            positive.

        extra (Dict): Extra dictionary array; functionality undetermined

    *[async]{.pre}[ ]{.w}*[[send_dropin_notification]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[title]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'AlexaAPI]{.pre} [Dropin]{.pre} [Notification\']{.pre}]{.default_value}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.send_dropin_notification "Permalink to this definition"){.headerlink}

    :   Send dropin notification to Alexa app for Alexa device.

        Push a message to mobile devices with the Alexa App. This can
        spawn a notification to drop in on a specific device.

        Args: message (string): The message to push to the mobile
        device. title (string): Title for push notification customer_id
        (string): CustomerId to use for sending. When none

        > <div>
        >
        > specified this defaults to the logged in user.
        >
        > </div>

        queue_delay (float, optional): The number of seconds to wait

        :   for commands to queue together. Defaults to 1.5. Must be
            positive.

        extra (Dict): Extra dictionary array; functionality undetermined

    *[async]{.pre}[ ]{.w}*[[send_mobilepush]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[title]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'AlexaAPI]{.pre} [Message\']{.pre}]{.default_value}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.send_mobilepush "Permalink to this definition"){.headerlink}

    :   Send mobile push to Alexa app.

        Push a message to mobile devices with the Alexa App. This
        probably should be a static method.

        Args: message (string): The message to push to the mobile
        device. title (string): Title for push notification customer_id
        (string): CustomerId to use for sending. When none

        > <div>
        >
        > specified this defaults to the logged in user.
        >
        > </div>

        queue_delay (float, optional): The number of seconds to wait

        :   for commands to queue together. Defaults to 1.5. Must be
            positive.

        extra (Dict): Extra dictionary array; functionality undetermined

    *[async]{.pre}[ ]{.w}*[[send_sequence]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[sequence]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[extra]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.send_sequence "Permalink to this definition"){.headerlink}

    :   Send sequence command.

        This allows some programatic control of Echo device using the
        behaviors API and is the basis of play_music, send_announcement,
        and send_tts.

        Args: sequence (string): The Alexa sequence. Supported list
        below. customer_id (string): CustomerId to use for
        authorization. When none

        > <div>
        >
        > specified this defaults to the logged in user. Used with
        > households where others may have their own music.
        >
        > </div>

        queue_delay (float, optional): The number of seconds to wait

        :   for commands to queue together. Defaults to 1.5. Must be
            positive.

        extra (Dict): Extra dictionary array; functionality undetermined
        [[\*\*]{#id2 .problematic}](#id1)kwargs : Each named variable
        must match a recognized Amazon variable

        > <div>
        >
        > within the operationPayload. Please see examples in
        > play_music, send_announcement, and send_tts. Variables with
        > value None are removed from the operationPayload. Variables
        > prefixed with "[[root\_]{#id8 .problematic}](#id7)" will be
        > added to the root node instead.
        >
        > </div>

        Supported sequences: Alexa.Weather.Play Alexa.Traffic.Play
        Alexa.FlashBriefing.Play Alexa.GoodMorning.Play
        Alexa.GoodNight.Play Alexa.SingASong.Play Alexa.TellStory.Play
        Alexa.FunFact.Play Alexa.Joke.Play Alexa.CleanUp.Play
        Alexa.Music.PlaySearchPhrase Alexa.Calendar.PlayTomorrow
        Alexa.Calendar.PlayToday Alexa.Calendar.PlayNext
        [https://github.com/custom-components/alexa_media_player/wiki#sequence-commands-versions--100](https://github.com/custom-components/alexa_media_player/wiki#sequence-commands-versions--100){.reference
        .external}

    *[async]{.pre}[ ]{.w}*[[send_tts]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[targets]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[List]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.send_tts "Permalink to this definition"){.headerlink}

    :   Send message for TTS at speaker.

        This is the old method which used Alexa Simon Says which did not
        work for WHA. This will not beep prior to sending.
        send_announcement should be used instead.

        Args: message (string): The message to speak. For canned
        messages, the message

        > <div>
        >
        > must start with alexa.cannedtts.speak as discovered in the
        > routines.
        >
        > </div>

        customer_id (string): CustomerId to use for authorization. When none

        :   specified this defaults to the logged in user. Used with
            households where others may have their own music.

        targets (list(string)): WARNING: This is currently non functional due

        :   to Alexa's API and is only included for future proofing.
            List of serialNumber or accountName to send the tts to. Only
            those in this AlexaAPI account will be searched. If None,
            announce will be self.

        queue_delay (float, optional): The number of seconds to wait

        :   for commands to queue together. Defaults to 1.5. Must be
            positive.

    *[async]{.pre}[ ]{.w}*[[set_background]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[url]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_background "Permalink to this definition"){.headerlink}

    :   Set background for Echo Show.

        Sets the background to Alexa App Photo with the specific https
        url.

        Args url (URL): valid https url for the image

        Returns Whether the command was successful.

    *[async]{.pre}[ ]{.w}*[[set_bluetooth]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mac]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_bluetooth "Permalink to this definition"){.headerlink}

    :   Pair with bluetooth device with mac address.

    *[async]{.pre}[ ]{.w}*[[set_dnd_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[state]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_dnd_state "Permalink to this definition"){.headerlink}

    :   Set Do Not Disturb state.

        Args: state (boolean): true or false

        Returns json

    *[async]{.pre}[ ]{.w}*[[set_guard_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[entity_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[state]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_guard_state "Permalink to this definition"){.headerlink}

    :   Set Guard state.

        Args: entity_id (Text): numeric ending of applianceId of RedRock
        Panel state (Text): AWAY, HOME queue_delay (float, optional):
        The number of seconds to wait

        > <div>
        >
        > for commands to queue together. Defaults to 1.5. Must be
        > positive.
        >
        > </div>

        Returns json

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[set_light_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[entity_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[power_on]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[True]{.pre}]{.default_value}*, *[[brightness]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[int]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[color_name]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[color_temperature_name]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_light_state "Permalink to this definition"){.headerlink}

    :   Set state of a light.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin
        entity_id (Text): Entity ID of The light. Not the Application
        ID. power_on (bool): Should the light be on or off. brightness
        (Optional\[int\]): 0-100 or None to leave as is color_name
        (Optional\[Text\]): The name of a color that Alexa supports in
        snake case. color_temperature_name (Optional\[Text\]): The name
        of a color temperature name that Alexa supports in snake case.

        Returns json

    *[async]{.pre}[ ]{.w}*[[set_media]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[data]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_media "Permalink to this definition"){.headerlink}

    :   Select the media player.

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[set_notifications]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[data]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_notifications "Permalink to this definition"){.headerlink}

    :   Update Alexa notification.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin data
        : Data to pass to notifications

        Returns json

    *[async]{.pre}[ ]{.w}*[[set_volume]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[volume]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}*, *[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.set_volume "Permalink to this definition"){.headerlink}

    :   Set volume.

        Args: volume (float): The volume between 0 and 1. customer_id
        (string): CustomerId to use for sending. When none

        > <div>
        >
        > specified this defaults to the logged in user.
        >
        > </div>

        queue_delay (float, optional): The number of seconds to wait

        :   for commands to queue together. Defaults to 1.5. Must be
            positive.

    *[async]{.pre}[ ]{.w}*[[shuffle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[setting]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.shuffle "Permalink to this definition"){.headerlink}

    :   Shuffle.

        setting (string) : true or false

    *[async]{.pre}[ ]{.w}[static]{.pre}[ ]{.w}*[[static_set_guard_state]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[entity_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*, *[[state]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Dict]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.static_set_guard_state "Permalink to this definition"){.headerlink}

    :   Set state of Alexa guard.

        Args: login (AlexaLogin): Successfully logged in AlexaLogin
        entity_id (Text): entityId of RedRock Panel state (Text):
        ARMED_AWAY, ARMED_STAY

        Returns json

    *[async]{.pre}[ ]{.w}*[[stop]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[customer_id]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Optional]{.pre}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[queue_delay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[float]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1.5]{.pre}]{.default_value}*, *[[all_devices]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bool]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[False]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.stop "Permalink to this definition"){.headerlink}

    :   Stop device playback.

        Keyword Arguments

        :   - **(default** (*all_devices {bool} \-- Whether all devices
              should be stopped*) -- {None})

            - **wait** (*queue_delay {float} \-- The number of seconds
              to*) -- for commands to queue together. Must be positive.
              (default: {1.5})

            - **(default** -- {False})

    [[update_login]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[bool]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaAPI.update_login "Permalink to this definition"){.headerlink}

    :   Update Login if it has changed.

        Args

        :   login (AlexaLogin): AlexaLogin to check

        Returns

        :   bool: True if change detected

<!-- -->

*[class]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexaProxy]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[base_url]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren}[¶](#alexapy.AlexaProxy "Permalink to this definition"){.headerlink}

:   Class to handle proxy login connections to Alexa.

    Inheritance

     graphviz
    Inheritance diagram of AlexaProxy


    [[autofill]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[items]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[dict]{.pre}]{.n}*, *[[html]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[str]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaProxy.autofill "Permalink to this definition"){.headerlink}

    :   Autofill input tags in form in html.

        Args

        :   html (Text): html to convert items (dict): Dictionary of
            values to fill

        Returns

        :   Text: html with values filled in

    [[change_login]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaProxy.change_login "Permalink to this definition"){.headerlink}

    :   Change login.

        Parameters

        :   **login**
            ([*AlexaLogin*](index.html#alexapy.AlexaLogin "alexapy.AlexaLogin"){.reference
            .internal}) -- AlexaLogin object to update after completion
            of proxy.

    *[async]{.pre}[ ]{.w}*[[test_amazon_url]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[resp]{.pre}]{.n}*, *[[data]{.pre}]{.n}*, *[[query]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Optional]{.pre}[[\[]{.pre}]{.p}[Union]{.pre}[[\[]{.pre}]{.p}[yarl.URL]{.pre}[[,]{.pre}]{.p}[ ]{.w}[str]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.AlexaProxy.test_amazon_url "Permalink to this definition"){.headerlink}

    :   Test for Alexa success.

        Args

        :   resp (httpx.Response): The aiohttp response. data
            (Dict\[Text, Any\]): Dictionary of all post data captured
            through proxy with overwrites for duplicate keys. query
            (Dict\[Text, Any\]): Dictionary of all query data with
            overwrites for duplicate keys.

        Returns

        :   Optional\[Union\[URL, Text\]\]: URL for a http 302 redirect
            or Text to display on success. None indicates test did not
            pass.

<!-- -->

*[class]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[WebsocketEchoClient]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[login]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[alexapy.alexalogin.AlexaLogin]{.pre}](index.html#alexapy.AlexaLogin "alexapy.alexalogin.AlexaLogin"){.reference .internal}]{.n}*, *[[msg_callback]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[alexapy.alexawebsocket.Message]{.pre}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[Coroutine]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[None]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}*, *[[open_callback]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[Coroutine]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[None]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}*, *[[close_callback]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[Coroutine]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[None]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}*, *[[error_callback]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[str]{.pre}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[Coroutine]{.pre}[[\[]{.pre}]{.p}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[,]{.pre}]{.p}[ ]{.w}[None]{.pre}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.n}*[)]{.sig-paren}[¶](#alexapy.WebsocketEchoClient "Permalink to this definition"){.headerlink}

:   WebSocket Client Class for Echo Devices.

    Based on code from openHAB:
    [https://github.com/openhab/openhab2-addons/blob/master/addons/binding/org.openhab.binding.amazonechocontrol/src/main/java/org/openhab/binding/amazonechocontrol/internal/WebSocketConnection.java](https://github.com/openhab/openhab2-addons/blob/master/addons/binding/org.openhab.binding.amazonechocontrol/src/main/java/org/openhab/binding/amazonechocontrol/internal/WebSocketConnection.java){.reference
    .external} which is further based on:
    [https://github.com/Apollon77/alexa-remote/blob/master/alexa-wsmqtt.js](https://github.com/Apollon77/alexa-remote/blob/master/alexa-wsmqtt.js){.reference
    .external}

    Inheritance

     graphviz
    Inheritance diagram of WebsocketEchoClient


    *[async]{.pre}[ ]{.w}*[[async_on_open]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.WebsocketEchoClient.async_on_open "Permalink to this definition"){.headerlink}

    :   Handle Async WebSocket Open.

    *[async]{.pre}[ ]{.w}*[[async_run]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.WebsocketEchoClient.async_run "Permalink to this definition"){.headerlink}

    :   Start Async WebSocket Listener.

    [[on_close]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[future]{.pre}]{.n}[[=]{.pre}]{.o}[[\'\']{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.WebsocketEchoClient.on_close "Permalink to this definition"){.headerlink}

    :   Handle WebSocket Close.

    [[on_error]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[error]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[str]{.pre}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\'Unspecified\']{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.WebsocketEchoClient.on_error "Permalink to this definition"){.headerlink}

    :   Handle WebSocket Error.

    *[async]{.pre}[ ]{.w}*[[on_message]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[bytes]{.pre}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.WebsocketEchoClient.on_message "Permalink to this definition"){.headerlink}

    :   Handle New Message.

    *[async]{.pre}[ ]{.w}*[[process_messages]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren} [[→]{.sig-return-icon} [[None]{.pre}]{.sig-return-typehint}]{.sig-return}[¶](#alexapy.WebsocketEchoClient.process_messages "Permalink to this definition"){.headerlink}

    :   Start Async WebSocket Listener.


 {#exceptions .section}
### [Exceptions](#id6){.toc-backref}[¶](#exceptions "Permalink to this headline"){.headerlink}

- [[`AlexapyConnectionError`{.xref .py .py-exc .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexapyConnectionError "alexapy.AlexapyConnectionError"){.reference
  .internal}: Define an error related to invalid requests.

- [[`AlexapyLoginCloseRequested`{.xref .py .py-exc .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexapyLoginCloseRequested "alexapy.AlexapyLoginCloseRequested"){.reference
  .internal}: Define an error related to requesting access to API after
  requested close.

- [[`AlexapyLoginError`{.xref .py .py-exc .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexapyLoginError "alexapy.AlexapyLoginError"){.reference
  .internal}: Define an error related to no longer being logged in.

- [[`AlexapyPyotpInvalidKey`{.xref .py .py-exc .docutils .literal
  .notranslate}]{.pre}](#alexapy.AlexapyPyotpInvalidKey "alexapy.AlexapyPyotpInvalidKey"){.reference
  .internal}: Define an error related to invalid 2FA key.

*[exception]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexapyConnectionError]{.pre}]{.sig-name .descname}[¶](#alexapy.AlexapyConnectionError "Permalink to this definition"){.headerlink}

:   Define an error related to invalid requests.

    Inheritance

     graphviz
    Inheritance diagram of AlexapyConnectionError


<!-- -->

*[exception]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexapyLoginCloseRequested]{.pre}]{.sig-name .descname}[¶](#alexapy.AlexapyLoginCloseRequested "Permalink to this definition"){.headerlink}

:   Define an error related to requesting access to API after requested
    close.

    Inheritance

     graphviz
    Inheritance diagram of AlexapyLoginCloseRequested


<!-- -->

*[exception]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexapyLoginError]{.pre}]{.sig-name .descname}[¶](#alexapy.AlexapyLoginError "Permalink to this definition"){.headerlink}

:   Define an error related to no longer being logged in.

    Inheritance

     graphviz
    Inheritance diagram of AlexapyLoginError


<!-- -->

*[exception]{.pre}[ ]{.w}*[[alexapy.]{.pre}]{.sig-prename .descclassname}[[AlexapyPyotpInvalidKey]{.pre}]{.sig-name .descname}[¶](#alexapy.AlexapyPyotpInvalidKey "Permalink to this definition"){.headerlink}

:   Define an error related to invalid 2FA key.

    Inheritance

     graphviz
    Inheritance diagram of AlexapyPyotpInvalidKey


:
::


 {#indices-and-tables .section}
# Indices and tables[¶](#indices-and-tables "Permalink to this headline"){.headerlink}

- [[Index]{.std .std-ref}](genindex.html){.reference .internal}

- [[Module Index]{.std .std-ref}](py-modindex.html){.reference
  .internal}

- [[Search Page]{.std .std-ref}](search.html){.reference .internal}


:
