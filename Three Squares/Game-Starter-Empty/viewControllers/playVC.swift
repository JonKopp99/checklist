//
//  playVC.swift
//  Game-Starter-Empty
//
//  Created by Jonathan Kopp on 10/4/18.
//  Copyright © 2018 Make School. All rights reserved.
//

import Foundation
import UIKit
import SpriteKit
import CoreGraphics

class playVC: UIViewController
{

    var daNum = 0.0
    var timer = Timer()
    @IBOutlet weak var playButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
        print("PlayViewLoaded")
        ///self.view.backgroundColor = #colorLiteral(red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0)
        scheduledTimerWithTimeInterval()
        
    }
    func scheduledTimerWithTimeInterval(){
        // Scheduling timer to Call the function "updateCounting" with the interval of 1 seconds
        timer = Timer.scheduledTimer(withTimeInterval: 0.05, repeats: true, block: {_ in self.drawBack()})
    }
    
    func drawBack()
    {
        if (daNum >= 1){
            daNum=0.0
        }
        else
        {
            daNum += 0.01
        }
        //color t=color(c,255,255);
        //let color = UIColor(displayP3Hue: CGFloat(daNum), saturation: 1, brightness: 1)
        let color = UIColor(hue: CGFloat(daNum), saturation: 1, brightness: 1, alpha: 1)
        self.playButton.backgroundColor = color
    }
    
}
