#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD605848ED7E69871 (ueno@gnu.org)
#
Name     : p11-kit
Version  : 0.23.22
Release  : 64
URL      : https://github.com/p11-glue/p11-kit/releases/download/0.23.22/p11-kit-0.23.22.tar.xz
Source0  : https://github.com/p11-glue/p11-kit/releases/download/0.23.22/p11-kit-0.23.22.tar.xz
Source1  : https://github.com/p11-glue/p11-kit/releases/download/0.23.22/p11-kit-0.23.22.tar.xz.sig
Summary  : Library and proxy module for properly loading and sharing PKCS#11 modules.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: p11-kit-bin = %{version}-%{release}
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-lib = %{version}-%{release}
Requires: p11-kit-libexec = %{version}-%{release}
Requires: p11-kit-license = %{version}-%{release}
Requires: p11-kit-services = %{version}-%{release}
Requires: ca-certs
Requires: findutils
BuildRequires : buildreq-meson
BuildRequires : ca-certs
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : intltool-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32libffi)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32libtasn1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtasn1)
Patch1: 0001-Added-P11_TRUST_PATHS-to-override-via-env.patch
Patch2: 0002-Use-p11-trust-instead-of-trust.patch

%description
# p11-kit
[![Build Status](https://travis-ci.org/p11-glue/p11-kit.svg?branch=master)](https://travis-ci.org/p11-glue/p11-kit) [![Coverage Status](https://img.shields.io/coveralls/p11-glue/p11-kit.svg)](https://coveralls.io/r/p11-glue/p11-kit) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1627/badge)](https://bestpractices.coreinfrastructure.org/en/projects/1627) [![Total alerts](https://img.shields.io/lgtm/alerts/g/p11-glue/p11-kit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/p11-glue/p11-kit/alerts/) [![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/p11-glue/p11-kit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/p11-glue/p11-kit/context:cpp)

%package bin
Summary: bin components for the p11-kit package.
Group: Binaries
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-libexec = %{version}-%{release}
Requires: p11-kit-license = %{version}-%{release}
Requires: p11-kit-services = %{version}-%{release}

%description bin
bin components for the p11-kit package.


%package data
Summary: data components for the p11-kit package.
Group: Data

%description data
data components for the p11-kit package.


%package dev
Summary: dev components for the p11-kit package.
Group: Development
Requires: p11-kit-lib = %{version}-%{release}
Requires: p11-kit-bin = %{version}-%{release}
Requires: p11-kit-data = %{version}-%{release}
Provides: p11-kit-devel = %{version}-%{release}
Requires: p11-kit = %{version}-%{release}

%description dev
dev components for the p11-kit package.


%package dev32
Summary: dev32 components for the p11-kit package.
Group: Default
Requires: p11-kit-lib32 = %{version}-%{release}
Requires: p11-kit-bin = %{version}-%{release}
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-dev = %{version}-%{release}

%description dev32
dev32 components for the p11-kit package.


%package doc
Summary: doc components for the p11-kit package.
Group: Documentation

%description doc
doc components for the p11-kit package.


%package lib
Summary: lib components for the p11-kit package.
Group: Libraries
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-libexec = %{version}-%{release}
Requires: p11-kit-license = %{version}-%{release}

%description lib
lib components for the p11-kit package.


%package lib32
Summary: lib32 components for the p11-kit package.
Group: Default
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-license = %{version}-%{release}

%description lib32
lib32 components for the p11-kit package.


%package libexec
Summary: libexec components for the p11-kit package.
Group: Default
Requires: p11-kit-license = %{version}-%{release}

%description libexec
libexec components for the p11-kit package.


%package license
Summary: license components for the p11-kit package.
Group: Default

%description license
license components for the p11-kit package.


%package services
Summary: services components for the p11-kit package.
Group: Systemd services

%description services
services components for the p11-kit package.


%prep
%setup -q -n p11-kit-0.23.22
cd %{_builddir}/p11-kit-0.23.22
%patch1 -p1
%patch2 -p1
pushd ..
cp -a p11-kit-0.23.22 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618351561
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --with-trust-paths=/var/cache/ca-certs --with-hash-impl=internal
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --with-trust-paths=/var/cache/ca-certs --with-hash-impl=internal   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1618351561
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/p11-kit
cp %{_builddir}/p11-kit-0.23.22/COPYING %{buildroot}/usr/share/package-licenses/p11-kit/6745330da3e7bde244b20b96a42eae659644e731
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/etc/pkcs11/pkcs11.conf.example
rm -f %{buildroot}%{_libdir}/p11-kit/trust-extract-compat
## install_append content
mv %{buildroot}/usr/bin/trust %{buildroot}/usr/bin/p11-trust
install -m 0755 trust-stub %{buildroot}/usr/bin/trust
# The libnssckbi.so alias for p11-kit-trust.so is needed for Chrome's NSS
# implementation. Note that "p11-kit-trust.so" is the SONAME, so the symlink
# chain must be libnssckbi.so -> p11-kit-trust.so -> pkcs11/p11-kit-trust.so to
# satisfy ldconfig rules.
ln -s p11-kit-trust.so %{buildroot}/usr/lib64/libnssckbi.so
ln -s pkcs11/p11-kit-trust.so %{buildroot}/usr/lib64/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/p11-kit
/usr/bin/p11-trust
/usr/bin/trust

%files data
%defattr(-,root,root,-)
/usr/share/p11-kit/modules/p11-kit-trust.module

%files dev
%defattr(-,root,root,-)
/usr/include/p11-kit-1/p11-kit/deprecated.h
/usr/include/p11-kit-1/p11-kit/iter.h
/usr/include/p11-kit-1/p11-kit/p11-kit.h
/usr/include/p11-kit-1/p11-kit/pin.h
/usr/include/p11-kit-1/p11-kit/pkcs11.h
/usr/include/p11-kit-1/p11-kit/pkcs11x.h
/usr/include/p11-kit-1/p11-kit/remote.h
/usr/include/p11-kit-1/p11-kit/uri.h
/usr/lib64/pkgconfig/p11-kit-1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32p11-kit-1.pc
/usr/lib32/pkgconfig/p11-kit-1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/p11-kit/config-example.html
/usr/share/gtk-doc/html/p11-kit/config-files.html
/usr/share/gtk-doc/html/p11-kit/config.html
/usr/share/gtk-doc/html/p11-kit/devel-building-style.html
/usr/share/gtk-doc/html/p11-kit/devel-building.html
/usr/share/gtk-doc/html/p11-kit/devel-commands.html
/usr/share/gtk-doc/html/p11-kit/devel-debugging.html
/usr/share/gtk-doc/html/p11-kit/devel-paths.html
/usr/share/gtk-doc/html/p11-kit/devel-testing.html
/usr/share/gtk-doc/html/p11-kit/devel.html
/usr/share/gtk-doc/html/p11-kit/gtk-doc.css
/usr/share/gtk-doc/html/p11-kit/home.png
/usr/share/gtk-doc/html/p11-kit/index.html
/usr/share/gtk-doc/html/p11-kit/left-insensitive.png
/usr/share/gtk-doc/html/p11-kit/left.png
/usr/share/gtk-doc/html/p11-kit/p11-kit-Deprecated.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-Future.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-Modules.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-PIN-Callbacks.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-URIs.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-Utilities.html
/usr/share/gtk-doc/html/p11-kit/p11-kit.devhelp2
/usr/share/gtk-doc/html/p11-kit/p11-kit.html
/usr/share/gtk-doc/html/p11-kit/pkcs11-conf.html
/usr/share/gtk-doc/html/p11-kit/reference.html
/usr/share/gtk-doc/html/p11-kit/remoting.html
/usr/share/gtk-doc/html/p11-kit/right-insensitive.png
/usr/share/gtk-doc/html/p11-kit/right.png
/usr/share/gtk-doc/html/p11-kit/sharing-managed.html
/usr/share/gtk-doc/html/p11-kit/sharing.html
/usr/share/gtk-doc/html/p11-kit/style.css
/usr/share/gtk-doc/html/p11-kit/tools.html
/usr/share/gtk-doc/html/p11-kit/trust-disable.html
/usr/share/gtk-doc/html/p11-kit/trust-glib-networking.html
/usr/share/gtk-doc/html/p11-kit/trust-module.html
/usr/share/gtk-doc/html/p11-kit/trust-nss.html
/usr/share/gtk-doc/html/p11-kit/trust.html
/usr/share/gtk-doc/html/p11-kit/up-insensitive.png
/usr/share/gtk-doc/html/p11-kit/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnssckbi.so
/usr/lib64/libp11-kit.so
/usr/lib64/libp11-kit.so.0
/usr/lib64/libp11-kit.so.0.3.0
/usr/lib64/p11-kit-proxy.so
/usr/lib64/p11-kit-trust.so
/usr/lib64/pkcs11/p11-kit-client.so
/usr/lib64/pkcs11/p11-kit-trust.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libp11-kit.so
/usr/lib32/libp11-kit.so.0
/usr/lib32/libp11-kit.so.0.3.0
/usr/lib32/p11-kit-proxy.so
/usr/lib32/pkcs11/p11-kit-client.so
/usr/lib32/pkcs11/p11-kit-trust.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/p11-kit/p11-kit-remote
/usr/libexec/p11-kit/p11-kit-server
/usr/libexec/p11-kit/trust-extract-compat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/p11-kit/6745330da3e7bde244b20b96a42eae659644e731

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/p11-kit-server.service
/usr/lib/systemd/user/p11-kit-server.socket
