[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Molecule CI/CD](https://github.com/nginxinc/ansible-role-nginx/workflows/Molecule%20CI/CD/badge.svg)](https://github.com/nginxinc/ansible-role-nginx/actions)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Community Support](https://badgen.net/badge/support/community/cyan?icon=awesome)](https://github.com/nginxinc/ansible-role-nginx/blob/main/SUPPORT.md)

# 👾 *Help make the NGINX Ansible role better by participating in our [survey](https://forms.office.com/Pages/ResponsePage.aspx?id=L_093Ttq0UCb4L-DJ9gcUKLQ7uTJaE1PitM_37KR881UM0NCWkY5UlE5MUYyWU1aTUcxV0NRUllJSC4u)!* 👾

# Ansible NGINX Role

This role installs NGINX Open Source, NGINX Plus, or the NGINX Amplify agent on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

## Requirements

### NGINX Plus (Optional)

If you wish to install NGINX Plus using this role, you will need to obtain an NGINX Plus license beforehand. *You do not need to do anything beforehand if you want to install NGINX OSS.*

### Ansible

- This role is developed and tested with [maintained](https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html) versions of Ansible core (above `2.12`).
- When using Ansible core, you will also need to install the following collections:

    ```yaml
    ---
    collections:
      - name: ansible.posix
        version: 1.5.4
      - name: community.general
        version: 6.4.0
      - name: community.crypto # Only required if you plan to install NGINX Plus
        version: 2.14.1
      - name: community.docker # Only required if you plan to use Molecule (see below)
        version: 3.4.7
    ```

    **Note:** You can alternatively install the Ansible community distribution (what is known as the "old" Ansible) if you don't want to manage individual collections.
- You will need to run this role as a root user using Ansible's `become` parameter. Make sure you have set up the appropriate permissions on your target hosts.
- Instructions on how to install Ansible can be found in the [Ansible website](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#upgrading-ansible-from-version-2-9-and-older-to-version-2-10-or-later).

### Jinja2

- This role uses Jinja2 templates. Ansible core installs Jinja2 by default, but depending on your install and/or upgrade path, you might be running an outdated version of Jinja2. The minimum version of Jinja2 required for the role to properly function is `3.1`.
- Instructions on how to install Jinja2 can be found in the [Jinja2 website](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation).

### Molecule (Optional)

- Molecule is used to test the various functionalities of the role. The recommended version of Molecule to test this role is `4.x`.
- Instructions on how to install Molecule can be found in the [Molecule website](https://molecule.readthedocs.io/en/latest/installation.html). *You will also need to install the Molecule Docker driver.*
- To run the NGINX Plus Molecule tests, you must copy your NGINX Plus license to the role's [`files/license`](https://github.com/nginxinc/ansible-role-nginx/blob/main/files/license/) folder.

  You can alternatively add your NGINX Plus repository certificate and key to the local environment. Run the following commands to export these files as base64-encoded variables and execute the Molecule tests:

  ```bash
  export NGINX_CRT=$( cat <path to your certificate file> | base64 )
  export NGINX_KEY=$( cat <path to your key file> | base64 )
  molecule test -s plus
  ```

## Installation

### Ansible Galaxy

To install the latest stable release of the role on your system, use:

```bash
ansible-galaxy install nginxinc.nginx
```

Alternatively, if you have already installed the role, update the role to the latest release:

```bash
ansible-galaxy install -f nginxinc.nginx
```

### Git

To pull the latest edge commit of the role from GitHub, use:

```bash
git clone https://github.com/nginxinc/ansible-role-nginx.git
```

## Platforms

The NGINX Ansible role supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html), [NGINX Plus](https://docs.nginx.com/nginx/technical-specs/), and the [NGINX Amplify agent](https://github.com/nginxinc/nginx-amplify-doc/blob/master/amplify-faq.md#21-what-operating-systems-are-supported):

### NGINX Open Source

```yaml
AlmaLinux:
  - 8
  - 9
Alpine:
  - 3.15
  - 3.16
  - 3.17
  - 3.18
Amazon Linux:
  - 2
CentOS:
  - 7.4+
Debian:
  - bullseye (11)
  - bookworm (12)
Oracle Linux:
  - 7
  - 8
  - 9
Red Hat:
  - 7.4+
  - 8
  - 9
Rocky Linux:
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - focal (20.04)
  - jammy (22.04)
  - lunar (23.04)
```

### NGINX Plus

```yaml
AlmaLinux:
  - 8
  - 9
Alpine:
  - 3.15
  - 3.16
  - 3.17
  - 3.18
Amazon Linux:
  - 2
CentOS:
  - 7.4+
Debian:
  - bullseye (11)
  - bookworm (12)
FreeBSD:
  - 12.1+
  - 13
Oracle Linux:
  - 7.4+
  - 8.1+
  - 9
Red Hat:
  - 7.4+
  - 8.1+
  - 9
Rocky Linux:
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - focal (20.04)
  - jammy (22.04)
```

### NGINX Amplify Agent

```yaml
Amazon Linux:
  - 2
Debian:
  - buster (10)
  - bullseye (11)
Red Hat:
  - 8
  - 9
Ubuntu:
  - bionic (18.04)
  - focal (20.04)
  - jammy (22.04)
```

**Note:** You can also use this role to compile NGINX Open Source from source, install NGINX Open Source on compatible yet unsupported platforms, or install NGINX Open Source on BSD systems at your own risk.

## Role Variables

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **[`defaults/main/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/main.yml)** | NGINX installation variables |
| **[`amplify.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/amplify.yml)** | NGINX Amplify agent installation variables |
| **[`bsd.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/bsd.yml)** | BSD installation variables |
| **[`logrotate.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/logrotate.yml)** | Logrotate configuration variables |
| **[`selinux.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/selinux.yml)** | SELinux configuration variables |
| **[`systemd.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/systemd.yml)** | Systemd configuration variables |

Similarly, descriptions and defaults for preset variables can be found in the **[`vars/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/main.yml)** | List of supported NGINX platforms, modules, and Linux installation variables |

## Example Playbooks

Working functional playbook examples can be found in the **[`molecule/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`default/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/default/converge.yml)** | Install a specific version of NGINX, install various NGINX supported modules, tweak systemd and set up logrotate |
| **[`distribution/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/distribution/converge.yml)** | Install NGINX from the distribution's package repository instead of NGINX's package repository |
| **[`downgrade/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/downgrade/converge.yml)** | Downgrade to a specific version of NGINX |
| **[`downgrade-plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/downgrade-plus/converge.yml)** | Downgrade to a specific version of NGINX Plus |
| **[`plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/plus/converge.yml)** | Install NGINX Plus and various NGINX Plus supported modules |
| **[`source/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/source/converge.yml)** | Install NGINX from source |
| **[`stable/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/stable/converge.yml)** | Install NGINX using the latest stable release |
| **[`uninstall/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/uninstall/converge.yml)** | Uninstall NGINX |
| **[`uninstall-plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/uninstall-plus/converge.yml)** | Uninstall NGINX Plus |
| **[`upgrade/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/upgrade/converge.yml)** | Upgrade NGINX |
| **[`upgrade-plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/upgrade-plus/converge.yml)** | Upgrade NGINX Plus |
| **[`version/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/version/converge.yml)** | Install a specific version of NGINX and various NGINX modules |

Do note that if you install this repository via Ansible Galaxy, you will have to replace the role variable in the sample playbooks from `ansible-role-nginx` to `nginxinc.nginx`.

For installing dynamic modules from source. Check [defaults/main/main.yml](defaults/main/main.yml).

Check the following ( `CMD|CTRL + F` ):

- nginx_install_dynamic_module_only
- nginx_compile_install_dynamic_modules
- nginx_dynamic_module_default
  
There is detailed examples of the usage.

Otherwise here a practical example:

```yaml
    # nginx_compile_install_dynamic_modules for dynamic modules from compile installation
    # ngx_addon_name: "" prop can be added.
    # - When not set, it would be set automatically. Setting it will override auto-detect.
    # - (addon name is in the config file in source root (make config))
    nginx_compile_install_dynamic_modules:
      ##
      # 🔥 mod_brotli 🔥 module
      # - https://github.com/google/ngx_brotli
      # - out modules names to load
      #   - ngx_http_brotli_filter_module
      #   - ngx_http_brotli_static_module
      ##
      - preset: "mod_brotli" # preset or name (sort of alias, if with name no url or download_cmds is provided)
        # --with-compat is required
        version: "master" # master contain a lot of updates, we can [fix a commit in place of master, if you want to apply no latest security]
        dest: "{{ nginx_install_source_dest }}"
        mode: "0600"
        module_mode: "0700"

      ##
      # 🔥 mod_security 🔥 module
      # - https://github.com/SpiderLabs/ModSecurity-nginx
      # - https://github.com/SpiderLabs/ModSecurity
      # (Check preset for details: .ansible/roles/nginxinc.nginx/tasks/modules/install-compile-dynamic-modules/download-prepare-dynamic-module.yml)
      # version:
      # - can be any release version the version should be set without v
      #    - ex: version: '1.0.3'
      #    - The release tarbal will be downloaded, and unpacked
      # Presets:
      # - mod_security_src (recommended one)
      #   - build the lib dep from source
      #   - If you build it once, you can save the build modules, and add it
      #      - Automatically when the lib is found installed, it wouldn't be built
      - preset: mod_security_src
        version: '1.0.3'
        preset_vars:
          lib: # modesecurity lib dependency params (Gonna be build from source)
            version: 'v3/master' # latest in master (default)
            # version: 'v3.0.10' # releases (https://github.com/SpiderLabs/ModSecurity/releases)
        dest: "{{ nginx_install_source_dest }}"
        mode: "0600"
        module_mode: "0700"
      # - mod_security doesn't build
      #   - install the lib dep using apt install libmodsecurity3
      ##
      # - preset: mod_security
      #   version: 'v1.0.3'
      #   dest: "{{ nginx_install_source_dest }}"
      #   mode: "0600"
      ##
      # 🔥 mod_passenger 🔥 module
      # - mod_passenger for nginx
      #   - src: https://github.com/phusion/passenger/archive/refs/tags/release-6.0.18.tar.gz
      # - passenger:
      #   - oss src repo: https://github.com/phusion/passenger/
      #   - src: https://www.phusionpassenger.com/library/install/nginx/install/oss/tarball/
      ##
      # 🔥🔥🔥 - Try later to build for ubuntu with docker
      # - preset: "mod_passenger" # we can use `preset` or `name` (if name, no url or download_cmds should be provided)
      #   # - any branch
      #   # - release branches are found in https://github.com/phusion/passenger/releases
      #   #   - have the format `release-<version>`
      #   version: "release-6.0.18"
      #   dest: "{{ nginx_install_source_dest }}"
      #   mode: "0600"

      ###
      # 🔥 mod_pagespeed 🔥 (https://www.modpagespeed.com/doc/build_ngx_pagespeed_from_source)
      # - requirements:
      #    - sudo apt-get install build-essential zlib1g-dev libpcre3 libpcre3-dev unzip uuid-dev
      ## ❌ Skipped, we do that another time or never (compiling from source, vps not enough memory, need to may be do it locally) ❌
      # - use bazel on master, and following travis ci (for building the psol lib)
      # Using mod_pagespeed preset
      # - preset_vars.psol.version: need to be a git branch https://github.com/apache/incubator-pagespeed-mod
      # - version: need to be a git branch https://github.com/apache/incubator-pagespeed-ngx
      #    - and its for ngx_pagespeed
      # - the mod_pagespeed (for psol) and ngx_pagespeed => need to be compatible
      #    - try to use the same branch
      #      - release (tag/release)
      #      - or not release (some branch ex: release-1.11.33.0-beta, master)
      # - preset: "mod_pagespeed"
      #   version: "master" # need to be a git branch
      #   preset_vars:
      #     psol:
      #       version: "master" # need to be a git branch
      #   dest: "{{ nginx_install_source_dest }}"
      #   mode: "0600"

      ##
      # 🔥 mod_geoip2 🔥 module
      # - does use git repo
      # - version:
      #   - You can set versions tags (release versions: 3.4, 3.3 ...)
      #   - You can set branches (mainly: master)
      #
      ##
      - preset: mod_geoip2
        version: "3.4" # master
        dest: "{{ nginx_install_source_dest }}"
        mode: "0600"
        module_mode: "0700"


    # nginx_compile_install_dynamic_modules_only: false # default false
```

Full example

```yaml
---
# -- Nginx and Nginx modules requirements
# - name: Install and set any Nginx or Nginx modules requirements
#   block:
#     # - name: Install needed packages
#     #   ansible.builtin.apt:
#     #     name:
#           # mod_passenger need them
#           # https://www.phusionpassenger.com/library/install/nginx/install/oss/tarball/
#           # - ruby
#           # - rake

# -- Nginx (installation and configuration)
- name: Install NGINX
  ansible.builtin.include_role:
    name: nginxinc.nginx
  vars:
    # Specify which type of NGINX you want to install.
    # Options are 'opensource' or 'plus'.
    # Default is 'opensource'.
    nginx_type: opensource

    # (Optional) Specify which version of NGINX you want to install.
    # Default is to install the latest release.
    # For NGINX Open Source you'll need to specify the relevant release like below (Ubuntu jammy example).
    # nginx_version: "=1.23.2-1~jammy"
    # For NGINX Plus you'll need to specify the R* release like below (Ubuntu jammy example).
    # nginx_version: "=28-1~jammy"
    nginx_version: "1.25.2"

    # Nginx service

    # Start NGINX service.
    # Default is true.
    nginx_start: true

    # Nginx systemd
    nginx_service_systemd_src: services/nginx.systemd # [TOCHECK]
    # nginx_service_upstart_src: services/nginx.upstart
    # nginx_service_upstart_conf_src: services/nginx.conf.upstart
    # nginx_service_sysvinit_src: services/nginx.sysvinit
    # nginx_service_openrc_src: services/nginx.openrc


    # Specify whether you want to install NGINX, upgrade to the latest version, or remove NGINX.
    # Can be used with `nginx_version` to fine tune control which version of NGINX is installed/used on each playbook execution.
    # Using 'install' will install the latest version (or 'nginx_version') of NGINX on a fresh install.
    # Using 'upgrade' will upgrade NGINX to the latest version (that matches your 'nginx_version') of NGINX on every playbook execution.
    # Using 'uninstall' will remove NGINX from your system.
    # Default is install.
    nginx_setup: install

    # Specify whether or not you want to manage the NGINX repositories.
    # Using 'true' will manage NGINX repositories.
    # Using 'false' will not manage the NGINX repositories, allowing them to be managed through other means.
    # Default is true
    nginx_manage_repo: true

    # 🔥 Specify repository origin for NGINX Open Source. 🔥
    # Only works if 'nginx_type' is set to 'opensource'.
    # Options are 'nginx_repository', 'source' or 'os_repository'.
    # When using 'os_repository' on CentOS/RHEL 7 based systems,
    # you will also need to install the EPEL repository (see the 'nginx_install_epel_release' variable below).
    # Default is nginx_repository.
    # ! nginx_repository => should install most of the modules
    # ! - if some module need to be installed and is no included => we should switch to install from `source`
    # ! - ref: https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/
    nginx_install_from: source

    # Specify which branch of NGINX Open Source you want to install.
    # Options are 'mainline' or 'stable'.
    # Only works if 'install_from' is set to 'nginx_repository' or 'source'.
    # Default is mainline.
    nginx_branch: mainline

    # Specify source install options for NGINX Open Source.
    # Options represent whether to install from source also or to install from packages (default).
    # These only apply if 'nginx_install_from' is set to 'source'.
    # 'nginx_install_source_build_tools' will install compiler and build tools from packages.
    # If set to false, you need to have these present.
    # For the required libraries, true means we will install from source and false means we will install using the default package manager.
    nginx_install_source_build_tools: true # Install using packages (apt for debian)
    nginx_install_source_pcre: false # from source (static)
    nginx_install_source_openssl: true # from source (static)
    nginx_install_source_zlib: true # from source (static)
    nginx_install_source_dest: /usr/share
    nginx_install_source_modules_path: "{{ ngx_modules_dir }}"
    nginx_install_source_configure_cmd_base: >-
      ./configure
      --conf-path={{ ngx_conf_dir }}/nginx.conf
      --error-log-path=/var/log/nginx/error.log
      --http-log-path=/var/log/nginx/access.log
      --lock-path=/var/lock/nginx.lock
      --modules-path={{ nginx_install_source_modules_path }}
      --prefix={{ bitwol_ngx_prefix }}
      --pid-path=/var/run/nginx.pid
      --user=nginx
      --with-mail=dynamic
      --with-stream
      --with-compat
      --with-file-aio
      --with-threads
    # nginx_install_source_extra_params: # Not needed if nginx_install_source_configure_cmd_base is set
    #   - --with-something
    #   - -anotherparam

    # 🔥🔥 Specify source install module for NGINX Open Source. 🔥🔥
    # You can select any of the static modules listed on http://nginx.org/en/docs/configure.html.
    # Format is '--with-*' where '*' should be used as static module name in the list below. (see an example below).
    # Default is 'http_ssl_module'. (DO NOT remove it if you need SSL support).
    # nginx_static_modules: [http_ssl_module]
    # nginx_static_modules: ['http_v2_module']  # Example for '--with-http_v2_module'
    nginx_static_modules:
      # - 'stream_ssl_module'
      # - 'stream_realip_module'
      # - 'stream_geoip_module'
      # - 'stream_geoip_module=dynamic'
      # - 'stream_ssl_preread_module'
            # module that allows extracting information from the
            # ClientHello message without terminating SSL/TLS. This module is not built by default.
      - 'mail_ssl_module'
      - 'http_ssl_module'
      - 'http_realip_module'
      - 'http_sub_module'
      - 'http_dav_module'
      - 'http_gzip_static_module'
      - 'http_stub_status_module'
      - 'http_v2_module'
      # - 'http_v3_module' # Still experimental, we don't have use for it yet (https://nginx.org/en/docs/http/ngx_http_v3_module.html)


    # Enable to true when you want to not install nginx, but only compile from source, install dynamic modules
    # Default is `false`
    # nginx_install_dynamic_module_only: false
    # nginx_install_dynamic_module_only: true


    # nginx_compile_install_dynamic_modules for dynamic modules from compile installation
    # ngx_addon_name: "" prop can be added.
    # - When not set, it would be set automatically. Setting it will override auto-detect.
    # - (addon name is in the config file in source root (make config))
    nginx_compile_install_dynamic_modules:
      ##
      # 🔥 mod_brotli 🔥 module
      # - https://github.com/google/ngx_brotli
      # - out modules names to load
      #   - ngx_http_brotli_filter_module
      #   - ngx_http_brotli_static_module
      ##
      - preset: "mod_brotli" # preset or name (sort of alias, if with name no url or download_cmds is provided)
        # --with-compat is required
        version: "master" # master contain a lot of updates, we can [fix a commit in place of master, if you want to apply no latest security]
        dest: "{{ nginx_install_source_dest }}"
        mode: "0600"
        module_mode: "0700"

      ##
      # 🔥 mod_security 🔥 module
      # - https://github.com/SpiderLabs/ModSecurity-nginx
      # - https://github.com/SpiderLabs/ModSecurity
      # (Check preset for details: .ansible/roles/nginxinc.nginx/tasks/modules/install-compile-dynamic-modules/download-prepare-dynamic-module.yml)
      # version:
      # - can be any release version the version should be set without v
      #    - ex: version: '1.0.3'
      #    - The release tarbal will be downloaded, and unpacked
      # Presets:
      # - mod_security_src (recommended one)
      #   - build the lib dep from source
      #   - If you build it once, you can save the build modules, and add it
      #      - Automatically when the lib is found installed, it wouldn't be built
      - preset: mod_security_src
        version: '1.0.3'
        preset_vars:
          lib: # modesecurity lib dependency params (Gonna be build from source)
            version: 'v3/master' # latest in master (default)
            # version: 'v3.0.10' # releases (https://github.com/SpiderLabs/ModSecurity/releases)
        dest: "{{ nginx_install_source_dest }}"
        mode: "0600"
        module_mode: "0700"
      # - mod_security doesn't build
      #   - install the lib dep using apt install libmodsecurity3
      ##
      # - preset: mod_security
      #   version: 'v1.0.3'
      #   dest: "{{ nginx_install_source_dest }}"
      #   mode: "0600"
      ##
      # 🔥 mod_passenger 🔥 module
      # - mod_passenger for nginx
      #   - src: https://github.com/phusion/passenger/archive/refs/tags/release-6.0.18.tar.gz
      # - passenger:
      #   - oss src repo: https://github.com/phusion/passenger/
      #   - src: https://www.phusionpassenger.com/library/install/nginx/install/oss/tarball/
      ##
      # 🔥🔥🔥 - Try later to build for ubuntu with docker
      # - preset: "mod_passenger" # we can use `preset` or `name` (if name, no url or download_cmds should be provided)
      #   # - any branch
      #   # - release branches are found in https://github.com/phusion/passenger/releases
      #   #   - have the format `release-<version>`
      #   version: "release-6.0.18"
      #   dest: "{{ nginx_install_source_dest }}"
      #   mode: "0600"

      ###
      # 🔥 mod_pagespeed 🔥 (https://www.modpagespeed.com/doc/build_ngx_pagespeed_from_source)
      # - requirements:
      #    - sudo apt-get install build-essential zlib1g-dev libpcre3 libpcre3-dev unzip uuid-dev
      ## ❌ Skipped, we do that another time or never (compiling from source, vps not enough memory, need to may be do it locally) ❌
      # - use bazel on master, and following travis ci (for building the psol lib)
      # Using mod_pagespeed preset
      # - preset_vars.psol.version: need to be a git branch https://github.com/apache/incubator-pagespeed-mod
      # - version: need to be a git branch https://github.com/apache/incubator-pagespeed-ngx
      #    - and its for ngx_pagespeed
      # - the mod_pagespeed (for psol) and ngx_pagespeed => need to be compatible
      #    - try to use the same branch
      #      - release (tag/release)
      #      - or not release (some branch ex: release-1.11.33.0-beta, master)
      # - preset: "mod_pagespeed"
      #   version: "master" # need to be a git branch
      #   preset_vars:
      #     psol:
      #       version: "master" # need to be a git branch
      #   dest: "{{ nginx_install_source_dest }}"
      #   mode: "0600"

      ##
      # 🔥 mod_geoip2 🔥 module
      # - does use git repo
      # - version:
      #   - You can set versions tags (release versions: 3.4, 3.3 ...)
      #   - You can set branches (mainly: master)
      #
      ##
      - preset: mod_geoip2
        version: "3.4" # master
        dest: "{{ nginx_install_source_dest }}"
        mode: "0600"
        module_mode: "0700"


    # nginx_compile_install_dynamic_modules_only: false # default false

    # (Optional) Specify repository for NGINX Open Source or NGINX Plus.
    # Only works if 'install_from' is set to 'nginx_repository' when installing NGINX Open Source.
    # Defaults are the official NGINX repositories.
    # nginx_repository: deb https://nginx.org/packages/mainline/debian/ buster nginx

    # Location of your NGINX Plus license in your local machine.
    # Default is the files folder within the NGINX Ansible role.
    # nginx_license:
    #   certificate: license/nginx-repo.crt
    #   key: license/nginx-repo.key

    # Set up NGINX Plus license before installation.
    # Default is true.
    # nginx_setup_license: true

    # Remove NGINX Plus license and repository after installation for security purposes.
    # Default is true.
    # nginx_remove_license: true

    # Specify whether or not you want this role to install the EPEL package when installing NGINX OSS in some distributions and some NGINX OSS/Plus modules.
    # Using 'true' will install EPEL.
    # Using 'false' will not install EPEL.
    # Default is true.
    # nginx_install_epel_release: true


    # 🔥🔥🔥 Install NGINX Dynamic Modules.
    # You can select any of the dynamic modules listed below. Beware of NGINX Plus only dynamic modules (these are marked).
    # Format is list with either the dynamic module name or a dictionary (see njs for an example).
    # When using a dictionary, the default value for state is present, and for version it's nginx_version if specified.
    # Default is an empty list (no dynamic modules are installed).
    # nginx_modules: []
      # - auth-spnego  # NGINX Plus
      # - brotli  # NGINX Plus
      # - cookie-flag  # NGINX Plus
      # - encrypted-session  # NGINX Plus
      # - geoip
      # - geoip2  # NGINX Plus
      # - headers-more  # NGINX Plus
      # - image-filter
      # - lua  # NGINX Plus
      # - ndk  # NGINX Plus
      # - name: njs  # Required
      #   state: present  # Optional
      #   version: =1.19.4+0.4.4-1~bionic  # Optional
      # - opentracing  # NGINX Plus
      # - passenger  # NGINX Plus
      # - perl
      # - prometheus  # NGINX Plus
      # - rtmp  # NGINX Plus
      # - set-misc  # NGINX Plus
      # - subs-filter  # NGINX Plus
      # - waf  # NGINX Plus
      # - xslt

    # Print NGINX configuration file to terminal after executing playbook.
    # nginx_debug_output: false

    # 🔥 Create custom logrotate config 🔥
    # - https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/logrotate.yml
    nginx_logrotate_conf_enable: false
    # nginx_logrotate_conf:
    #   paths:
    #     - /var/log/nginx/*.log
    #     - "{{ bitwol_ngx_logs_dir }}/*.log"
    #   options:
    #     - size 50M
    #     - missingok
    #     - rotate 10
    #     - compress
    #     - delaycompress
    #     - notifempty
    #     - create 0644 www-data adm # Changes nginx logs permissions
    #     - sharedscripts


    # 🔥 Enable systemd modifications 🔥
    # - https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/systemd.yml
    # ** ALL of the following variables are ignored unless this is set to true **
    # nginx_service_modify: false

    # Remove the override file completely
    # nginx_service_clean: false

    # Override the systemd directory
    # Default is /etc/systemd/system/nginx.service.d
    # nginx_service_overridepath: /etc/systemd/system/nginx.service.d

    # Override the systemd filename
    # Default is override.conf
    # nginx_service_overridefilename: override.conf

    # Set service timeout for systemd systems in seconds
    # [Service]
    # TimeoutStartSec=90
    # TimeoutStopSec=90
    # Default is to comment this out
    # nginx_service_timeoutstartsec: 90
    # nginx_service_timeoutstopsec: 90

    # Set the restart policy for systemd systems
    # Values = no (default), on-failure, on-abnormal, on-watchdog, on-abort, always
    # [Service]
    # Restart=on-failure
    # Default is to comment this out
    nginx_service_restart: on-failure

    # Set the restart timer in seconds
    # [Service]
    # RestartSec=5s
    # Default is to comment this out
    nginx_service_restartsec: 5s

    # 🔥 With that we can add more params for nginx unit service
    # - need to be set to rue and the file need to be set as well
    # Enable a custom systemd override file
    # ** This could break the service **
    # Setting this to true disables custom values above
    # nginx_service_custom: false

    # Filename and path for systemd override file
    # Setting this will overwrite existing override file
    # nginx_service_custom_file: "{{ role_path }}/files/services/nginx.override.conf"
```

## Other NGINX Ansible Collections and Roles

You can find the Ansible NGINX Core collection of roles to install and configure NGINX Open Source, NGINX Plus, and NGINX App Protect [here](https://github.com/nginxinc/ansible-collection-nginx).

You can find the Ansible NGINX configuration role to configure NGINX [here](https://github.com/nginxinc/ansible-role-nginx-config).

You can find the Ansible NGINX App Protect role to install and configure NGINX App Protect WAF and NGINX App Protect DoS [here](https://github.com/nginxinc/ansible-role-nginx-app-protect).

You can find the Ansible NGINX Unit role to install NGINX Unit [here](https://github.com/nginxinc/ansible-role-nginx-unit).

## License

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/main/LICENSE)

## Author Information

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

[Tom Gamull](https://github.com/magicalyak)

&copy; [F5, Inc.](https://www.f5.com/) 2018 - 2023
