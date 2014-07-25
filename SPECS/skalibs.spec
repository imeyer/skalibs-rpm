Name:		skalibs
Version:	1.6.0.0
Release:	1%{?dist}
Summary:	skalibs is a package centralizing the free software / open source C development files used for building all software at skarnet.org: it contains essentially general-purpose libraries. You will need to install skalibs if you plan to build skarnet.org software. The point is that you won't have to download and compile big libraries everytime you need to build a package: do it only once.

Group:		System Environment/Libraries
License:	ISC
URL:		http://skarnet.org/software/skalibs/index.html
Source0:	http://skarnet.org/software/skalibs/%{name}-%{version}.tar.gz
patch0:		remove-command-from-conf-defaultpath.diff
patch1:		update-package-export-to-support-DESTDIR.diff

BuildRequires:  glibc

%description


%prep
%setup -qn prog/%{name}-%{version}
# We want to use FHS so remove flag-slashpackage
%{__rm} -f %{_builddir}/prog/%{name}-%{version}/conf-compile/flag-slashpackage
%patch0 -p 1
%patch1 -p 1

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
%config /etc/leapsecs.dat
/lib/libbiguint.so
/lib/libbiguint.so.1
/lib/libbiguint.so.1.6
/lib/libbiguint.so.1.6.0.0
/lib/libbiguint.so.api.6.0
/lib/libdatastruct.so
/lib/libdatastruct.so.1
/lib/libdatastruct.so.1.6
/lib/libdatastruct.so.1.6.0.0
/lib/libdatastruct.so.api.6.0
/lib/librandom.so
/lib/librandom.so.1
/lib/librandom.so.1.6
/lib/librandom.so.1.6.0.0
/lib/librandom.so.api.6.0
/lib/libstdcrypto.so
/lib/libstdcrypto.so.1
/lib/libstdcrypto.so.1.6
/lib/libstdcrypto.so.1.6.0.0
/lib/libstdcrypto.so.api.6.0
/lib/libstddjb.so
/lib/libstddjb.so.1
/lib/libstddjb.so.1.6
/lib/libstddjb.so.1.6.0.0
/lib/libstddjb.so.api.6.0
/lib/libunixonacid.so
/lib/libunixonacid.so.1
/lib/libunixonacid.so.1.6
/lib/libunixonacid.so.1.6.0.0
/lib/libunixonacid.so.api.6.0
/usr/include/skalibs/alloc.h
/usr/include/skalibs/allreadwrite.h
/usr/include/skalibs/ancillary.h
/usr/include/skalibs/avlnode.h
/usr/include/skalibs/avltree.h
/usr/include/skalibs/avltreen.h
/usr/include/skalibs/biguint.h
/usr/include/skalibs/bitarray.h
/usr/include/skalibs/bufalloc.h
/usr/include/skalibs/buffer.h
/usr/include/skalibs/bytestr.h
/usr/include/skalibs/cdb.h
/usr/include/skalibs/cdb_make.h
/usr/include/skalibs/datastruct.h
/usr/include/skalibs/direntry.h
/usr/include/skalibs/diuint.h
/usr/include/skalibs/diuint32.h
/usr/include/skalibs/djbtime.h
/usr/include/skalibs/djbunix.h
/usr/include/skalibs/env.h
/usr/include/skalibs/envalloc.h
/usr/include/skalibs/environ.h
/usr/include/skalibs/error.h
/usr/include/skalibs/fmtscan.h
/usr/include/skalibs/functypes.h
/usr/include/skalibs/gccattributes.h
/usr/include/skalibs/genalloc.h
/usr/include/skalibs/genset.h
/usr/include/skalibs/gensetdyn.h
/usr/include/skalibs/genwrite.h
/usr/include/skalibs/getpeereid.h
/usr/include/skalibs/gidstuff.h
/usr/include/skalibs/iobuffer.h
/usr/include/skalibs/iopause.h
/usr/include/skalibs/ip46.h
/usr/include/skalibs/kolbak.h
/usr/include/skalibs/lolstdio.h
/usr/include/skalibs/md5.h
/usr/include/skalibs/mininetstring.h
/usr/include/skalibs/netstring.h
/usr/include/skalibs/nonposix.h
/usr/include/skalibs/nsig.h
/usr/include/skalibs/random.h
/usr/include/skalibs/rc4.h
/usr/include/skalibs/rrandom.h
/usr/include/skalibs/segfault.h
/usr/include/skalibs/select.h
/usr/include/skalibs/selfpipe.h
/usr/include/skalibs/setgroups.h
/usr/include/skalibs/sgetopt.h
/usr/include/skalibs/sha1.h
/usr/include/skalibs/sha256.h
/usr/include/skalibs/shglob.h
/usr/include/skalibs/sig.h
/usr/include/skalibs/siovec.h
/usr/include/skalibs/skaclient.h
/usr/include/skalibs/skalibs-config.h
/usr/include/skalibs/skamisc.h
/usr/include/skalibs/socket.h
/usr/include/skalibs/sredfa.h
/usr/include/skalibs/stdcrypto.h
/usr/include/skalibs/stddjb.h
/usr/include/skalibs/stralloc.h
/usr/include/skalibs/strerr.h
/usr/include/skalibs/strerr2.h
/usr/include/skalibs/surf.h
/usr/include/skalibs/sysdeps.h
/usr/include/skalibs/tai.h
/usr/include/skalibs/uint.h
/usr/include/skalibs/uint16.h
/usr/include/skalibs/uint32.h
/usr/include/skalibs/uint64.h
/usr/include/skalibs/ulong.h
/usr/include/skalibs/unirandom.h
/usr/include/skalibs/unix-timed.h
/usr/include/skalibs/unix-transactional.h
/usr/include/skalibs/unixonacid.h
/usr/include/skalibs/ushort.h
/usr/include/skalibs/webipc.h
/usr/lib/skalibs/libbiguint.a
/usr/lib/skalibs/libdatastruct.a
/usr/lib/skalibs/librandom.a
/usr/lib/skalibs/libstdcrypto.a
/usr/lib/skalibs/libstddjb.a
/usr/lib/skalibs/libunixonacid.a
/usr/lib/skalibs/sysdeps/rt.lib
/usr/lib/skalibs/sysdeps/socket.lib
/usr/lib/skalibs/sysdeps/sysclock.lib
/usr/lib/skalibs/sysdeps/sysdeps
/usr/lib/skalibs/sysdeps/sysdeps.h
/usr/lib/skalibs/sysdeps/systype
/usr/lib/skalibs/sysdeps/taianow.lib
/usr/lib/skalibs/sysdeps/util.lib

%changelog

