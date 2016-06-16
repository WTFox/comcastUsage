comcastUsage
============

A simple command line script for seeing how much data have you left until you blow through Comcast's data cap.


Installation
------------

`comcastUsage` is not currently in PyPI, so you'll have to install it using `pip`:

```sh
$> git clone https://github.com/WTFox/comcastUsage.git
$> cd comcastUsage
$> pip install .
```

Usage
-----

After installing, you can check your Comcast data usage by running `comcast-usage` from a terminal.
Running this command will give you output that looks like this:

```
$> comcast-usage 

Comcast/Xfinity Data Usage for the Month.
--------------------------------------------------------------------------------
54% of data used
62% through the month.
114 GBs remaining until 01/31/16.
186 GBs / 300GBs used.
--------------------------------------------------------------------------------
```

`comcastUsage` depends on two environment variables `COMCAST_USERNAME` AND `COMCAST_PASSWORD`.
As you can probably guess, your Comcast username goes in `COMCAST_USERNAME` and
your Comcast password goes in `COMCAST_PASSWORD`.
You can add these to your `bash` initialization script...

```sh
# ~/.bashrc

# ...snip...

export COMCAST_USERNAME=example.user@comcast.com
export COMCAST_PASSWORD=supersecretpassword

# ...snip ...
```

or they can passed on the command line each time you run the script:

```sh
$> COMCAST_USERNAME="example.user@comcast.com COMCAST_PASSWORD="supersecretpassword" comcast-usage
```

Author
------

`comcastUsage` was written by Anthony Fox.

